# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import arabic_reshaper


def _reshaping_test(test):
    for i, case in enumerate(test.cases):
        def t(): test.assertEqual(case[1], test.reshaper.reshape(case[0]))
        if hasattr(test, 'subTest'):
            with test.subTest(i=i, case=case[0]):
                t()
        else:
            t()


class TestDefaultReshaping(unittest.TestCase):
    def setUp(self):
        self.reshaper = arabic_reshaper.default_reshaper
        self.cases = (
            ('السلام عليكم', 'ﺍﻟﺴﻼﻡ ﻋﻠﻴﻜﻢ'),
            ('السَلَاْمٌ عَلَيْكُمْ', 'ﺍﻟﺴﻼﻡ ﻋﻠﻴﻜﻢ'),
            ('اللغة العربية هي أكثر اللغات', 'ﺍﻟﻠﻐﺔ ﺍﻟﻌﺮﺑﻴﺔ ﻫﻲ ﺃﻛﺜﺮ ﺍﻟﻠﻐﺎﺕ'),
            ('تحدثاً ونطقاً ضمن مجموعة', 'ﺗﺤﺪﺛﺎ ﻭﻧﻄﻘﺎ ﺿﻤﻦ ﻣﺠﻤﻮﻋﺔ'),
            ('اللغات السامية', 'ﺍﻟﻠﻐﺎﺕ ﺍﻟﺴﺎﻣﻴﺔ'),
            ('العربية لغة رسمية في',  'ﺍﻟﻌﺮﺑﻴﺔ ﻟﻐﺔ ﺭﺳﻤﻴﺔ ﻓﻲ'),
            ('كل دول الوطن العربي',  'ﻛﻞ ﺩﻭﻝ ﺍﻟﻮﻃﻦ ﺍﻟﻌﺮﺑﻲ'),
            ('إضافة إلى كونها لغة',  'ﺇﺿﺎﻓﺔ ﺇﻟﻰ ﻛﻮﻧﻬﺎ ﻟﻐﺔ'),
            ('رسمية في تشاد وإريتريا',  'ﺭﺳﻤﻴﺔ ﻓﻲ ﺗﺸﺎﺩ ﻭﺇﺭﻳﺘﺮﻳﺎ'),
            ('وإسرائيل. وهي إحدى اللغات',  'ﻭﺇﺳﺮﺍﺋﻴﻞ. ﻭﻫﻲ ﺇﺣﺪﻯ ﺍﻟﻠﻐﺎﺕ'),
            ('الرسمية الست في منظمة',  'ﺍﻟﺮﺳﻤﻴﺔ ﺍﻟﺴﺖ ﻓﻲ ﻣﻨﻈﻤﺔ'),
            ('الأمم المتحدة، ويُحتفل',  'ﺍﻷﻣﻢ ﺍﻟﻤﺘﺤﺪﺓ، ﻭﻳﺤﺘﻔﻞ'),
            ('باليوم العالمي للغة العربية',  'ﺑﺎﻟﻴﻮﻡ ﺍﻟﻌﺎﻟﻤﻲ ﻟﻠﻐﺔ ﺍﻟﻌﺮﺑﻴﺔ'),
            ('في 18 ديسمبر كذكرى اعتماد',  'ﻓﻲ 18 ﺩﻳﺴﻤﺒﺮ ﻛﺬﻛﺮﻯ ﺍﻋﺘﻤﺎﺩ'),
            ('العربية بين لغات العمل في',  'ﺍﻟﻌﺮﺑﻴﺔ ﺑﻴﻦ ﻟﻐﺎﺕ ﺍﻟﻌﻤﻞ ﻓﻲ'),
            ('الأمم المتحدة.', 'ﺍﻷﻣﻢ ﺍﻟﻤﺘﺤﺪﺓ.'),
        )

    def test_reshaping(self):
        _reshaping_test(self)


class TestReshapingWithHarakat(unittest.TestCase):
    def setUp(self):
        self.reshaper = arabic_reshaper.ArabicReshaper({
            'delete_harakat': False
        })
        self.cases = (
            ('السَلَاْمٌ عَلَيْكُمْ', 'ﺍﻟﺴَﻼَْﻡٌ ﻋَﻠَﻴْﻜُﻢْ'),
            ('اللغة العربية هي أكثر اللغات', 'ﺍﻟﻠﻐﺔ ﺍﻟﻌﺮﺑﻴﺔ ﻫﻲ ﺃﻛﺜﺮ ﺍﻟﻠﻐﺎﺕ'),
            ('تحدثاً ونطقاً ضمن مجموعة', 'ﺗﺤﺪﺛﺎً ﻭﻧﻄﻘﺎً ﺿﻤﻦ ﻣﺠﻤﻮﻋﺔ'),
            ('اللغات السامية', 'ﺍﻟﻠﻐﺎﺕ ﺍﻟﺴﺎﻣﻴﺔ'),
            ('العربية لغة رسمية في',  'ﺍﻟﻌﺮﺑﻴﺔ ﻟﻐﺔ ﺭﺳﻤﻴﺔ ﻓﻲ'),
            ('كل دول الوطن العربي',  'ﻛﻞ ﺩﻭﻝ ﺍﻟﻮﻃﻦ ﺍﻟﻌﺮﺑﻲ'),
            ('إضافة إلى كونها لغة',  'ﺇﺿﺎﻓﺔ ﺇﻟﻰ ﻛﻮﻧﻬﺎ ﻟﻐﺔ'),
            ('رسمية في تشاد وإريتريا',  'ﺭﺳﻤﻴﺔ ﻓﻲ ﺗﺸﺎﺩ ﻭﺇﺭﻳﺘﺮﻳﺎ'),
            ('وإسرائيل. وهي إحدى اللغات',  'ﻭﺇﺳﺮﺍﺋﻴﻞ. ﻭﻫﻲ ﺇﺣﺪﻯ ﺍﻟﻠﻐﺎﺕ'),
            ('الرسمية الست في منظمة',  'ﺍﻟﺮﺳﻤﻴﺔ ﺍﻟﺴﺖ ﻓﻲ ﻣﻨﻈﻤﺔ'),
            ('الأمم المتحدة، ويُحتفل',  'ﺍﻷﻣﻢ ﺍﻟﻤﺘﺤﺪﺓ، ﻭﻳُﺤﺘﻔﻞ'),
            ('باليوم العالمي للغة العربية',  'ﺑﺎﻟﻴﻮﻡ ﺍﻟﻌﺎﻟﻤﻲ ﻟﻠﻐﺔ ﺍﻟﻌﺮﺑﻴﺔ'),
            ('في 18 ديسمبر كذكرى اعتماد',  'ﻓﻲ 18 ﺩﻳﺴﻤﺒﺮ ﻛﺬﻛﺮﻯ ﺍﻋﺘﻤﺎﺩ'),
            ('العربية بين لغات العمل في',  'ﺍﻟﻌﺮﺑﻴﺔ ﺑﻴﻦ ﻟﻐﺎﺕ ﺍﻟﻌﻤﻞ ﻓﻲ'),
            ('الأمم المتحدة.', 'ﺍﻷﻣﻢ ﺍﻟﻤﺘﺤﺪﺓ.'),
        )

    def test_reshaping(self):
        _reshaping_test(self)


class TestReshapingWithHarakatWithoutLigatures(unittest.TestCase):
    def setUp(self):
        self.reshaper = arabic_reshaper.ArabicReshaper({
            'delete_harakat': False,
            'support_ligatures': False
        })
        self.cases = (
            ('السَلَاْمٌ عَلَيْكُمْ', 'ﺍﻟﺴَﻠَﺎْﻡٌ ﻋَﻠَﻴْﻜُﻢْ'),
            ('اللغة العربية هي أكثر اللغات', 'ﺍﻟﻠﻐﺔ ﺍﻟﻌﺮﺑﻴﺔ ﻫﻲ ﺃﻛﺜﺮ ﺍﻟﻠﻐﺎﺕ'),
            ('تحدثاً ونطقاً ضمن مجموعة', 'ﺗﺤﺪﺛﺎً ﻭﻧﻄﻘﺎً ﺿﻤﻦ ﻣﺠﻤﻮﻋﺔ'),
            ('اللغات السامية', 'ﺍﻟﻠﻐﺎﺕ ﺍﻟﺴﺎﻣﻴﺔ'),
            ('العربية لغة رسمية في',  'ﺍﻟﻌﺮﺑﻴﺔ ﻟﻐﺔ ﺭﺳﻤﻴﺔ ﻓﻲ'),
            ('كل دول الوطن العربي',  'ﻛﻞ ﺩﻭﻝ ﺍﻟﻮﻃﻦ ﺍﻟﻌﺮﺑﻲ'),
            ('إضافة إلى كونها لغة',  'ﺇﺿﺎﻓﺔ ﺇﻟﻰ ﻛﻮﻧﻬﺎ ﻟﻐﺔ'),
            ('رسمية في تشاد وإريتريا',  'ﺭﺳﻤﻴﺔ ﻓﻲ ﺗﺸﺎﺩ ﻭﺇﺭﻳﺘﺮﻳﺎ'),
            ('وإسرائيل. وهي إحدى اللغات',  'ﻭﺇﺳﺮﺍﺋﻴﻞ. ﻭﻫﻲ ﺇﺣﺪﻯ ﺍﻟﻠﻐﺎﺕ'),
            ('الرسمية الست في منظمة',  'ﺍﻟﺮﺳﻤﻴﺔ ﺍﻟﺴﺖ ﻓﻲ ﻣﻨﻈﻤﺔ'),
            ('الأمم المتحدة، ويُحتفل',  'ﺍﻟﺄﻣﻢ ﺍﻟﻤﺘﺤﺪﺓ، ﻭﻳُﺤﺘﻔﻞ'),
            ('باليوم العالمي للغة العربية',  'ﺑﺎﻟﻴﻮﻡ ﺍﻟﻌﺎﻟﻤﻲ ﻟﻠﻐﺔ ﺍﻟﻌﺮﺑﻴﺔ'),
            ('في 18 ديسمبر كذكرى اعتماد',  'ﻓﻲ 18 ﺩﻳﺴﻤﺒﺮ ﻛﺬﻛﺮﻯ ﺍﻋﺘﻤﺎﺩ'),
            ('العربية بين لغات العمل في',  'ﺍﻟﻌﺮﺑﻴﺔ ﺑﻴﻦ ﻟﻐﺎﺕ ﺍﻟﻌﻤﻞ ﻓﻲ'),
            ('الأمم المتحدة.', 'ﺍﻟﺄﻣﻢ ﺍﻟﻤﺘﺤﺪﺓ.'),
        )

    def test_reshaping(self):
        _reshaping_test(self)


class TestReshapingSomeLigatures(unittest.TestCase):
    def setUp(self):
        self.reshaper = arabic_reshaper.ArabicReshaper({
            'delete_tatweel': True,
            'ARABIC LIGATURE BISMILLAH AR-RAHMAN AR-RAHEEM': True,
            'ARABIC LIGATURE JALLAJALALOUHOU': True,
            'ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM': True,
            'ARABIC LIGATURE ALLAH ': True,
            'ARABIC LIGATURE AKBAR': True,
            'ARABIC LIGATURE ALAYHE': True,
            'ARABIC LIGATURE MOHAMMAD': True,
            'ARABIC LIGATURE RASOUL': True,
            'ARABIC LIGATURE SALAM': True,
            'ARABIC LIGATURE SALLA': True,
            'ARABIC LIGATURE WASALLAM': True,
        })
        self.cases = (
            ('إِنَّهُ مِن سُلَيْمَانَ '
             'وَإِنَّهُ بِسْمِ اللّـَهِ '
             'الرَّحْمَـٰنِ الرَّحِيمِ ﴿٣٠﴾ '
             'أَلَّا تَعْلُوا عَلَيَّ '
             'وَأْتُونِي مُسْلِمِينَ ﴿٣١﴾',

             'ﺇﻧﻪ ﻣﻦ ﺳﻠﻴﻤﺎﻥ ﻭﺇﻧﻪ ﷽ ﴿٣٠﴾ '
             'ﺃﻻ ﺗﻌﻠﻮﺍ ﻋﻠﻲ ﻭﺃﺗﻮﻧﻲ ﻣﺴﻠﻤﻴﻦ ﴿٣١﴾'),

            ('فَذَكِّرْ إِنَّمَا أَنتَ'
             ' مُذَكِّرٌ ﴿٢١﴾ لَّسْتَ'
             ' عَلَيْهِم بِمُصَيْطِرٍ ﴿٢٢﴾'
             ' إِلَّا مَن تَوَلَّىٰ'
             ' وَكَفَرَ ﴿٢٣﴾ فَيُعَذِّبُهُ'
             ' اللَّـهُ الْعَذَابَ'
             ' الْأَكْبَرَ ﴿٢٤﴾',

             'ﻓﺬﻛﺮ ﺇﻧﻤﺎ ﺃﻧﺖ'
             ' ﻣﺬﻛﺮ ﴿٢١﴾ ﻟﺴﺖ'
             ' ﻋﻠﻴﻬﻢ ﺑﻤﺼﻴﻄﺮ ﴿٢٢﴾'
             ' ﺇﻻ ﻣﻦ ﺗﻮﻟﻰ'
             ' ﻭﻛﻔﺮ ﴿٢٣﴾ ﻓﻴﻌﺬﺑﻪ'
             ' ﷲ ﺍﻟﻌﺬﺍﺏ'
             ' ﺍﻷﻛﺒﺮ ﴿٢٤﴾'),

            ('محمد رسول الله صلى الله عليه وسلم',
             'ﷴ ﷶ ﷲ ﷺ'),

            ('الله جل جلاله',
             'ﷲ ﷻ'),

            ('محمد رسول الله عليه صلى الله وسلم',
             'ﷴ ﷶ ﷲ ﷷ ﷹ ﷲ ﷸ'),
        )

    def test_reshaping(self):
        _reshaping_test(self)

if __name__ == '__main__':
    unittest.main()