#!/usr/bin/env python3
"""Import all question data from l6-l9 Python modules + đề cương JS into unified bank.json + curriculum.json"""
import sys, json, re, html

# Subject classification by grade+lesson
SUBJECT_MAP = {
    6: {range(1,8+1):'Mở đầu', range(9,39+1):'Hóa', range(40,51+1):'Lý', range(52,55+1):'Sinh'},
    7: {range(1,2+1):'Mở đầu', range(3,7+1):'Hóa', range(8,20+1):'Lý', range(21,42+1):'Sinh'},
    8: {range(1,1+1):'Mở đầu', range(2,12+1):'Hóa', range(13,29+1):'Lý', range(30,47+1):'Sinh'},
    9: {range(1,1+1):'Mở đầu', range(2,4+1):'Lý', range(5,10+1):'Lý', range(11,13+1):'Lý',
        range(14,15+1):'Lý', range(16,17+1):'Lý', range(18,27+1):'Hóa', range(28,35+1):'Hóa',
        range(36,48+1):'Sinh', range(49,51+1):'Sinh'},
}

def get_subject(grade, lesson_num):
    for rng, subj in SUBJECT_MAP.get(grade, {}).items():
        if lesson_num in rng:
            return subj
    return 'Khác'

# Level assignment for mc questions (indices 0-2 NB, 3-5 TH, 6-7 VD)
def mc_level(idx, total=8):
    if total <= 4:
        if idx < 2: return 'NB'
        if idx < 3: return 'TH'
        return 'VD'
    # 8 questions pattern
    if idx < 3: return 'NB'
    if idx < 6: return 'TH'
    return 'VD'

def parse_mc_options(opts):
    """Parse options list, identify correct answer marked with *"""
    parsed = []
    correct = -1
    for i, o in enumerate(opts):
        o = str(o).strip()
        if o.startswith('*'):
            correct = i
            o = o[1:].strip()
        parsed.append(o)
    return parsed, correct

def import_python_lessons(grade, modules_dir, module_names, prefix_map):
    """Import lessons from Python modules (l6/l7/l8/l9)"""
    questions = []
    lessons_info = []

    sys.path.insert(0, modules_dir)
    for mod_name in module_names:
        try:
            if mod_name in sys.modules:
                del sys.modules[mod_name]
            mod = __import__(mod_name)
        except Exception as e:
            print(f"  Skip {mod_name}: {e}")
            continue

        for attr_name in sorted(dir(mod)):
            obj = getattr(mod, attr_name)
            if not isinstance(obj, dict) or 'num' not in obj or 'mc' not in obj:
                continue

            L = obj
            lesson_num = L['num']
            subject = get_subject(grade, lesson_num)

            lessons_info.append({
                'grade': grade, 'lesson': lesson_num,
                'title': L.get('title',''), 'en': L.get('en',''),
                'subject': subject, 'icon': L.get('icon',''),
                'theory': L.get('br', []),
                'fact': L.get('fact',''), 'job': L.get('job',''),
            })

            # MC questions
            mc_list = L.get('mc', [])
            mc_note = L.get('mc_note', '')
            for i, mc in enumerate(mc_list):
                stem = mc[0]
                opts, correct = parse_mc_options(mc[1])
                explanation = mc[2] if len(mc) > 2 else ''
                level = mc_level(i, len(mc_list))

                questions.append({
                    'grade': grade, 'lesson': lesson_num, 'subject': subject,
                    'type': 'mc', 'level': level,
                    'stem': stem, 'options': opts, 'answer': correct,
                    'explanation': explanation,
                    'source': f'phieu_l{grade}'
                })

            # DS (Đúng/Sai)
            ds = L.get('ds')
            if ds and isinstance(ds, tuple) and len(ds) == 2:
                ds_stem, ds_items = ds
                items_data = []
                for it in ds_items:
                    items_data.append({
                        'text': it[0], 'answer': it[1],
                        'explanation': it[2] if len(it) > 2 else ''
                    })
                questions.append({
                    'grade': grade, 'lesson': lesson_num, 'subject': subject,
                    'type': 'ds', 'level': 'TH',
                    'stem': ds_stem, 'items': items_data,
                    'source': f'phieu_l{grade}'
                })

            # TL (Tự luận)
            for tl in L.get('tl', []):
                lvl = tl.get('lvl', 'cb')
                level = 'NB' if lvl == 'cb' else 'TH' if lvl == 'nc' else 'VD'
                questions.append({
                    'grade': grade, 'lesson': lesson_num, 'subject': subject,
                    'type': 'tl', 'level': level,
                    'stem': tl.get('q',''),
                    'sub': tl.get('sub', []),
                    'answer': tl.get('a', ''),
                    'source': f'phieu_l{grade}'
                })

            # TT (Thực tiễn)
            for tt in L.get('tt', []):
                questions.append({
                    'grade': grade, 'lesson': lesson_num, 'subject': subject,
                    'type': 'tt', 'level': 'VD',
                    'stem': (tt.get('t','') + ' ' + tt.get('q','')).strip(),
                    'answer': tt.get('a', ''),
                    'source': f'phieu_l{grade}'
                })

    sys.path.pop(0)
    return questions, lessons_info

# GK1 import (p1-p4 for KHTN 9)
def import_gk1():
    questions = []
    sys.path.insert(0, '/home/claude/gk1')

    for pname in ['p1','p2','p3','p4']:
        try:
            if pname in sys.modules:
                del sys.modules[pname]
            mod = __import__(pname)
        except:
            continue

        # Find the P dict
        P = None
        for attr in dir(mod):
            obj = getattr(mod, attr)
            if isinstance(obj, dict) and 'mc' in obj:
                P = obj
                break
        if not P:
            continue

        lesson_num = P.get('num', 0)
        subject = P.get('subject', 'Lý')
        levels = P.get('levels', [3,3,2])
        nb_count = levels[0] if len(levels)>0 else 3
        th_count = levels[1] if len(levels)>1 else 3

        # MC is a list of {dc, q, o, e}
        mc_list = P.get('mc', [])
        for i, mc in enumerate(mc_list):
            stem = mc.get('q', '')
            opts_raw = mc.get('o', [])
            opts, correct = parse_mc_options(opts_raw)
            explanation = mc.get('e', '')
            if i < nb_count: level = 'NB'
            elif i < nb_count + th_count: level = 'TH'
            else: level = 'VD'
            questions.append({
                'grade': 9, 'lesson': lesson_num, 'subject': subject,
                'type': 'mc', 'level': level,
                'stem': stem, 'options': opts, 'answer': correct,
                'explanation': explanation, 'source': 'gk1_khtn9'
            })

        # DS
        for ds in P.get('ds', []):
            items_data = []
            for it in ds.get('it', []):
                if isinstance(it, (list, tuple)):
                    items_data.append({'text': it[0], 'answer': it[1],
                                       'explanation': it[2] if len(it)>2 else ''})
                elif isinstance(it, dict):
                    items_data.append({'text': it.get('text',''), 'answer': it.get('v',''),
                                       'explanation': it.get('why','')})
            questions.append({
                'grade': 9, 'lesson': lesson_num, 'subject': subject,
                'type': 'ds', 'level': 'TH',
                'stem': ds.get('q',''), 'items': items_data, 'source': 'gk1_khtn9'
            })

        for sa in P.get('sa', []):
            questions.append({
                'grade': 9, 'lesson': lesson_num, 'subject': subject,
                'type': 'tl', 'level': 'TH',
                'stem': sa.get('q',''), 'sub': sa.get('sub', []),
                'answer': sa.get('a', ''), 'source': 'gk1_khtn9'
            })

        for tl in P.get('tl', []):
            if not isinstance(tl, dict): continue
            questions.append({
                'grade': 9, 'lesson': lesson_num, 'subject': subject,
                'type': 'tl', 'level': 'VD',
                'stem': tl.get('q',''), 'sub': tl.get('sub', []),
                'answer': tl.get('a', ''), 'source': 'gk1_khtn9'
            })

        for tt in P.get('tt', []):
            if not isinstance(tt, dict): continue
            questions.append({
                'grade': 9, 'lesson': lesson_num, 'subject': subject,
                'type': 'tt', 'level': 'VD',
                'stem': (tt.get('t','') + ' ' + tt.get('q','')).strip(),
                'answer': tt.get('a', ''), 'source': 'gk1_khtn9'
            })

    sys.path.pop(0)
    return questions


def main():
    all_questions = []
    all_lessons = []

    # l6
    print("Importing KHTN 6...")
    q, l = import_python_lessons(6, '/home/claude/l6', ['ch1','ch8','ch9','ch10'], {})
    all_questions.extend(q)
    all_lessons.extend(l)
    print(f"  {len(q)} questions, {len(l)} lessons")

    # l7
    print("Importing KHTN 7...")
    q, l = import_python_lessons(7, '/home/claude/l7', ['ch3','ch4','ch5','ch6'], {})
    all_questions.extend(q)
    all_lessons.extend(l)
    print(f"  {len(q)} questions, {len(l)} lessons")

    # l8
    print("Importing KHTN 8...")
    q, l = import_python_lessons(8, '/home/claude/l8', ['k3','k4','k5','k6'], {})
    all_questions.extend(q)
    all_lessons.extend(l)
    print(f"  {len(q)} questions, {len(l)} lessons")

    # l9
    print("Importing KHTN 9...")
    q, l = import_python_lessons(9, '/home/claude/l9', ['n1','n2','n3','n4','n5'], {})
    all_questions.extend(q)
    all_lessons.extend(l)
    print(f"  {len(q)} questions, {len(l)} lessons")

    # GK1
    print("Importing GK1 KHTN 9...")
    q = import_gk1()
    all_questions.extend(q)
    print(f"  {len(q)} questions")

    # Assign IDs
    for i, q in enumerate(all_questions):
        q['id'] = f'q{i+1:04d}'

    # Build curriculum
    curriculum = build_curriculum(all_lessons)

    # Save
    with open('/home/claude/khoweb/bank.json', 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=1)

    with open('/home/claude/khoweb/curriculum.json', 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, ensure_ascii=False, indent=1)

    print(f"\nTotal: {len(all_questions)} questions saved to bank.json")
    print(f"Curriculum: {len(curriculum)} grades saved to curriculum.json")

    # Stats
    for g in [6,7,8,9]:
        gq = [q for q in all_questions if q['grade'] == g]
        by_type = {}
        for q in gq:
            by_type[q['type']] = by_type.get(q['type'], 0) + 1
        print(f"  Lớp {g}: {len(gq)} câu — {by_type}")


def build_curriculum(lessons_data):
    """Build curriculum structure from imported lessons + hardcoded KNTT structure"""

    KNTT = {
        6: [
            ("Mở đầu", [(1,"Giới thiệu về Khoa học tự nhiên"),(2,"Các phép đo"),(3,"Quy tắc an toàn trong phòng thực hành"),
                         (4,"Sử dụng kính lúp"),(5,"Sử dụng kính hiển vi quang học"),
                         (6,"Đo chiều dài, khối lượng và thời gian"),(7,"Đo nhiệt độ"),(8,"Thang nhiệt độ")]),
            ("Chất và sự biến đổi", [(9,"Sự đa dạng của chất"),(10,"Các thể của chất và sự chuyển thể"),(11,"Oxygen. Không khí"),
                                     (12,"Một số vật liệu thông dụng"),(13,"Một số nguyên liệu thông dụng"),(14,"Một số lương thực – thực phẩm"),
                                     (15,"Một số nhiên liệu thông dụng"),(16,"Hỗn hợp và dung dịch"),(17,"Tách chất ra khỏi hỗn hợp")]),
            ("Năng lượng và sự biến đổi (Vật lý)", [(40,"Lực là gì?"),(41,"Biểu diễn lực"),(42,"Biến dạng của lò xo"),
                                                    (43,"Trọng lượng, lực hấp dẫn"),(44,"Lực ma sát"),(45,"Lực cản của nước")]),
            ("Năng lượng và sự biến đổi (tiếp)", [(46,"Năng lượng"),(47,"Nhiên liệu và năng lượng tái tạo"),(48,"Sự truyền nhiệt"),(49,"Sự dẫn nhiệt"),(50,"Sự đối lưu"),(51,"Bức xạ nhiệt")]),
            ("Trái Đất và bầu trời", [(52,"Chuyển động nhìn thấy của Mặt Trời"),(53,"Các hình dạng nhìn thấy của Mặt Trăng"),(54,"Hệ Mặt Trời"),(55,"Ngân Hà")]),
        ],
        7: [
            ("Nguyên tử – Nguyên tố hóa học", [(3,"Nguyên tử"),(4,"Nguyên tố hóa học"),(5,"Sơ lược về bảng tuần hoàn các nguyên tố hóa học")]),
            ("Phân tử", [(6,"Phân tử – Đơn chất – Hợp chất"),(7,"Hóa trị và công thức hóa học")]),
            ("Tốc độ", [(8,"Tốc độ chuyển động"),(9,"Đo tốc độ"),(10,"Đồ thị quãng đường – thời gian"),(11,"Tốc độ và an toàn giao thông")]),
            ("Âm thanh", [(12,"Sóng âm"),(13,"Độ to và độ cao của âm"),(14,"Phản xạ âm. Chống ô nhiễm tiếng ồn")]),
            ("Ánh sáng", [(15,"Sự truyền ánh sáng"),(16,"Phản xạ ánh sáng"),(17,"Ảnh của vật qua gương phẳng")]),
            ("Từ", [(18,"Từ trường"),(19,"Từ trường Trái Đất"),(20,"Nam châm điện")]),
            ("Trao đổi chất và chuyển hóa năng lượng ở sinh vật", [(21,"Quang hợp ở thực vật"),(22,"Các yếu tố ảnh hưởng đến quang hợp"),
                                                                    (23,"Hô hấp tế bào ở thực vật"),(24,"Trao đổi nước và chất dinh dưỡng ở thực vật"),(25,"Trao đổi nước và chất dinh dưỡng ở động vật")]),
        ],
        8: [
            ("Mở đầu", [(1,"Nhắc lại một số kiến thức KHTN 7")]),
            ("Phản ứng hóa học", [(2,"Biến đổi vật lí và biến đổi hóa học"),(3,"Phản ứng hóa học và năng lượng"),(4,"Mol và tỉ khối"),(5,"Dung dịch và nồng độ"),(6,"Tốc độ phản ứng và chất xúc tác"),(7,"Định luật bảo toàn khối lượng và phương trình hóa học")]),
            ("Một số hợp chất thông dụng", [(8,"Acid"),(9,"Base. Thang pH"),(10,"Oxide"),(11,"Muối"),(12,"Phân bón hóa học")]),
            ("Khối lượng riêng – Áp suất", [(13,"Khối lượng riêng"),(14,"Thực hành đo khối lượng riêng"),(15,"Áp suất trên một bề mặt"),(16,"Áp suất chất lỏng"),(17,"Áp suất khí quyển")]),
            ("Tác dụng làm quay của lực", [(18,"Moment lực"),(19,"Đòn bẩy và ứng dụng")]),
            ("Điện", [(20,"Hiện tượng nhiễm điện"),(21,"Dòng điện, nguồn điện"),(22,"Mạch điện đơn giản"),(23,"Tác dụng của dòng điện"),(24,"Cường độ dòng điện và hiệu điện thế"),(25,"Mắc mạch điện nối tiếp, song song")]),
            ("Nhiệt", [(26,"Năng lượng nhiệt và nội năng"),(27,"Sự truyền nhiệt"),(28,"Sự nóng chảy và sự đông đặc"),(29,"Sự bay hơi và sự ngưng tụ")]),
            ("Sinh học cơ thể người", [(30,"Khái quát về cơ thể người"),(31,"Hệ vận động ở người"),(32,"Dinh dưỡng và tiêu hóa ở người"),(33,"Máu và hệ tuần hoàn"),(34,"Hệ hô hấp ở người"),(35,"Hệ bài tiết ở người"),(36,"Hệ thần kinh và giác quan ở người"),(37,"Hệ nội tiết ở người"),(38,"Da và điều hòa thân nhiệt"),(39,"Sinh sản ở người"),(40,"Sức khỏe sinh sản vị thành niên")]),
            ("Sinh vật và môi trường", [(41,"Cơ thể sinh vật là một thể thống nhất"),(42,"Môi trường và các nhân tố sinh thái"),(43,"Quần thể sinh vật"),(44,"Quần xã sinh vật"),(45,"Hệ sinh thái"),(46,"Sinh quyển"),(47,"Cân bằng tự nhiên")]),
        ],
        9: [
            ("Mở đầu", [(1,"Mở đầu")]),
            ("Năng lượng cơ học", [(2,"Động năng. Thế năng"),(3,"Cơ năng"),(4,"Công và công suất")]),
            ("Điện", [(5,"Điện trở. Định luật Ohm"),(6,"Đoạn mạch nối tiếp, song song"),(7,"Năng lượng điện, công suất điện"),(8,"Thực hành: đo điện trở"),(9,"An toàn điện"),(10,"Mạch điện trong nhà")]),
            ("Quang học", [(11,"Hiện tượng khúc xạ ánh sáng"),(12,"Thấu kính"),(13,"Mắt. Các tật của mắt")]),
            ("Hóa vô cơ", [(14,"Phi kim"),(15,"Tính chất chung của kim loại")]),
            ("Điện từ", [(16,"Cảm ứng điện từ"),(17,"Máy phát điện và động cơ điện")]),
            ("Kim loại", [(18,"Sự khác nhau cơ bản giữa phi kim và kim loại"),(19,"Tính chất hóa học của kim loại"),(20,"Dãy hoạt động hóa học"),(21,"Hợp kim – Sự ăn mòn kim loại và bảo vệ")]),
            ("Hợp chất hữu cơ – Hydrocarbon", [(22,"Giới thiệu về hợp chất hữu cơ"),(23,"Alkane"),(24,"Nguồn nhiên liệu từ hydrocarbon"),(25,"Alkene, alkyne và Arene")]),
            ("Hợp chất hữu cơ có nhóm chức", [(26,"Ethanol"),(27,"Acetic acid")]),
            ("Polymer, Protein, Carbohydrate, Lipid", [(28,"Polymer"),(29,"Protein và amino acid"),(30,"Carbohydrate"),(31,"Lipid"),(32,"Ôn tập Hóa hữu cơ")]),
            ("Vật liệu, nhiên liệu, nguyên liệu, lương thực–thực phẩm", [(33,"Khai thác tài nguyên từ vỏ Trái Đất"),(34,"Vấn đề năng lượng và nhiên liệu"),(35,"Ôn tập tổng hợp")]),
            ("Di truyền học", [(36,"Khái quát về di truyền học"),(37,"Các quy luật di truyền của Mendel"),(38,"Nucleic acid và gene"),(39,"Tái bản DNA và phiên mã"),(40,"Dịch mã và đột biến gene"),(41,"Nhiễm sắc thể"),(42,"Đột biến nhiễm sắc thể"),(43,"Di truyền học với con người"),(44,"Ứng dụng công nghệ di truyền"),(45,"Ôn tập di truyền")]),
            ("Tiến hóa", [(46,"Bằng chứng tiến hóa"),(47,"Chọn lọc tự nhiên"),(48,"Tiến hóa của loài người")]),
            ("Sinh thái", [(49,"Hệ sinh thái"),(50,"Cân bằng tự nhiên"),(51,"Bảo vệ môi trường")]),
        ],
    }

    # Build lookup from imported lessons
    imported = {}
    for l in lessons_data:
        key = (l['grade'], l['lesson'])
        imported[key] = l

    result = {}
    for grade, chapters in KNTT.items():
        grade_data = []
        for ch_title, bais in chapters:
            ch = {'chapter': ch_title, 'lessons': []}
            for num, title in bais:
                info = imported.get((grade, num), {})
                lesson = {
                    'num': num, 'title': title,
                    'en': info.get('en', ''),
                    'icon': info.get('icon', ''),
                    'subject': info.get('subject', get_subject(grade, num)),
                    'hasQuestions': (grade, num) in imported,
                }
                if info.get('theory'):
                    lesson['theory'] = info['theory']
                if info.get('fact'):
                    lesson['fact'] = info['fact']
                if info.get('job'):
                    lesson['job'] = info['job']
                ch['lessons'].append(lesson)
            grade_data.append(ch)
        result[str(grade)] = grade_data

    return result


if __name__ == '__main__':
    main()
