from Flaskerizer_src.structure_directory import StructureDirectory
import Flaskerizer_src.Examples.Alstar_example as Example
import Flaskerizer_src.Tests as Tests
from Flaskerizer_src.config import CONFIGURATION
import flaskerizer
import unittest
import os
import shutil

class TestStructureDirectory(unittest.TestCase):
    maxDiff = None # reveals difference between test strings and "gold standard" strings

    def setUp(self):
        '''Instantiates an object 'test' from the StructureDirectory class. Tests are written to test both cases where
        the config.py CONFIGURATION['large_app_structure'] is set to either True or False.
        '''
        CONFIGURATION['app_name'] = 'Test_application'
        self.test = StructureDirectory(templates_path= os.path.dirname(Example.__file__),
                                       top_level_path= os.path.dirname(Example.__file__))
        if CONFIGURATION['large_app_structure'] == False:
            self.flaskerized_app_dir = os.path.join(os.path.dirname(flaskerizer.__file__),
                                                    os.path.basename('Test_application'))
            self.gold_standard_dir = os.path.join(os.path.dirname(Tests.__file__),
                                             os.path.basename('testing_files'),
                                             os.path.basename('small_Test_application_test_folder'))
        elif CONFIGURATION['large_app_structure'] == True:
            self.flaskerized_app_dir = os.path.join(os.path.join(os.path.dirname(flaskerizer.__file__),
                                                                 os.path.basename('Test_application')),
                                                                 os.path.basename('Test_application'))
            self.gold_standard_dir = os.path.join(os.path.dirname(Tests.__file__),
                                                  os.path.basename('testing_files'),
                                                  os.path.basename('large_Test_application_test_folder'))



    def test_mkdir(self):
        '''Tests that mkdir creates a folder named static and a folder named templates. Also test that the subfolders
        of static "css, fons, img, and js" are created.
        '''
        self.test.mkdir()
        self.assertTrue(os.path.exists(os.path.join(self.flaskerized_app_dir,
                                                    os.path.basename('static'))))
        self.assertTrue(os.path.exists(os.path.join(self.flaskerized_app_dir,
                                                    os.path.basename('static'),
                                                    os.path.basename('css'))))
        self.assertTrue(os.path.exists(os.path.join(self.flaskerized_app_dir,
                                                    os.path.basename('static'),
                                                    os.path.basename('fonts'))))
        self.assertTrue(os.path.exists(os.path.join(self.flaskerized_app_dir,
                                                    os.path.basename('static'),
                                                    os.path.basename('img'))))
        self.assertTrue(os.path.exists(os.path.join(self.flaskerized_app_dir,
                                                    os.path.basename('static'),
                                                    os.path.basename('js'))))
        self.assertTrue(os.path.exists(os.path.join(self.flaskerized_app_dir,
                                                    os.path.basename('templates'))))



    def test_detect_and_migrate_html_files(self):
        '''
        Confirms that detect_and_migrate_html_files migrates the correct number of files with extension .html
        from the Example bootstrap template directory to the 'templates; folder of the Test_application directory
        by comparing to the number of .html files in the 'templates' folder of a "gold_standard"
        respective Test_application_test_folder.
        '''
        self.test.mkdir()
        migrate_dict = self.test.detect_static_files()
        self.test.migrate_files(migrate_dict)
        self.test.detect_and_migrate_html_files()
        test_dir = os.path.join(self.flaskerized_app_dir,
                                        os.path.basename('templates'))
        if CONFIGURATION['large_app_structure'] == False:
            gold_standard_dir = os.path.join(self.gold_standard_dir,
                                             os.path.basename('templates'))
        elif CONFIGURATION['large_app_structure'] == True:
            gold_standard_dir = os.path.join(self.gold_standard_dir,
                                             os.path.basename('Test_application'),
                                             os.path.basename('templates'))

        test_file_list = []
        gold_standard_file_list = []
        for dir in [test_dir, gold_standard_dir]:
            for file in os.listdir(dir):
                if file.endswith('.html'):
                    if dir == test_dir:
                        test_file_list.append(file)
                    if dir == gold_standard_dir:
                        gold_standard_file_list.append(file)
        self.assertEqual(len(test_file_list), len(gold_standard_file_list))


    def test_migrate_files(self):
        '''Tests that migrate_files migrates the correct number of files from the Example bootstrap template directory
         to the Test_application directory. This is done by walking through the Test_application directory with os.walk
         and counting the number of files with a particular set of extensions (see extensions list) and comparing this
         number to the number of files gotten from walking through a "gold_standard" respective Test_application_test_folder.
        '''
        migrate_dict = self.test.detect_static_files()
        self.test.migrate_files(migrate_dict)
        extensions = ['.js', '.css', '.jpg', '.png', 'gif', '.ico', '.otf',
                      '.eot', '.svg', '.ttf', '.woff', '.woff2']
        test_dir = self.flaskerized_app_dir
        gold_standard_dir = os.path.join(os.path.dirname(Tests.__file__),
                                         os.path.basename('testing_files'),
                                        os.path.basename('small_Test_application_test_folder'))
        test_file_list = []
        gold_standard_file_list = []
        for dir in [test_dir, gold_standard_dir]:
            for path, subdir, files in os.walk(dir):
                for name in files:
                    for extension in extensions:
                        if name.endswith(extension):
                            if dir == test_dir:
                                test_file_list.append(name)
                            if dir == gold_standard_dir:
                                gold_standard_file_list.append(name)
        self.assertEqual(len(test_file_list), len(gold_standard_file_list))



for state in [True, False]:
    CONFIGURATION['large_app_structure'] = state #Tests are run under both CONFIGURATION['large_app_structure'] == True or False
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStructureDirectory)
    unittest.TextTestRunner().run(suite)
