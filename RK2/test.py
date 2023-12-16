import unittest
from main import *


class RK2_test(unittest.TestCase):
    Langs = [Lang(1, 'C++', 1985, 1),
             Lang(2, 'Python', 1991, 2),
             Lang(3, 'Java', 1995, 3),
             Lang(4, 'C', 1972, 4),
             Lang(5, 'Go', 2003, 4),
             Lang(6, 'PhP', 1995, 5),
             Lang(7, 'JavaScript', 1995, 4)
             ]

    IDEs = [IDE(1, 'CLion'),
            IDE(2, 'PyCharm'),
            IDE(3, 'IntelliJ'),
            IDE(4, 'VSCode'),
            IDE(5, 'PhP_sreda')]

    Lang_IDE = [LangIDE(1, 1),
                LangIDE(2, 2),
                LangIDE(3, 3),
                LangIDE(1, 4),
                LangIDE(4, 4),
                LangIDE(5, 4),
                LangIDE(6, 5),
                LangIDE(7, 4)]

    def test_1(self):
        one_to_many = [(l.name, l.year, i.name)
                       for l in Langs
                       for i in IDEs
                       if l.ide_id == i.id]
        ans1 = []
        for i in one_to_many:
            if i[0][0] == "P":
                ans1.append(i[0])
        self.assertEqual(ans1, ['Python', 'PhP'])

    def test_2(self):
        one_to_many = [(l.name, l.year, i.name)
                       for l in Langs
                       for i in IDEs
                       if l.ide_id == i.id]
        ans2_uns = []
        for instr in IDEs:
            instr_langs = list(filter(lambda i: i[2] == instr.name, one_to_many))
            if len(instr_langs) > 0:
                years = [year for _, year, _ in instr_langs]
                max_ = max(years)
                ans2_uns.append((instr.name, max_))
        ans2 = sorted(ans2_uns, key=itemgetter(1))
        self.assertEqual(ans2, [('CLion', 1985), ('PyCharm', 1991), ('IntelliJ', 1995),
                                ('PhP_sreda', 1995), ('VSCode', 2003)])

    def test_3(self):
        many_to_many_temp = [(i.name, li.ide_id, li.lang_id)
                             for i in IDEs
                             for li in Lang_IDE
                             if i.id == li.ide_id
                             ]
        many_to_many = [(l.name, l.year, ide_name)
                        for ide_name, ide_id, lang_id in many_to_many_temp
                        for l in Langs if l.id == lang_id]
        ans3 = sorted(many_to_many, key=lambda item: (item[2], item[1]))
        self.assertEqual(ans3, [('C++', 1985, 'CLion'), ('Java', 1995, 'IntelliJ'), ('PhP', 1995, 'PhP_sreda'),
                                ('Python', 1991, 'PyCharm'), ('C', 1972, 'VSCode'), ('C++', 1985, 'VSCode'),
                                ('JavaScript', 1995, 'VSCode'), ('Go', 2003, 'VSCode')])


if __name__ == '__main__':
    unittest.main()
