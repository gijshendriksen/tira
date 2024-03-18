from tira.third_party_integrations import extract_to_be_executed_notebook_from_command_or_none, extract_previous_stages_from_notebook, parse_ast_extract_assignment, parse_extraction_of_tira_approach, extract_previous_stages_from_docker_image
from pathlib import Path
import unittest

TEST_DIR = Path(__file__).parent.resolve()

class JupyterNotebookPipelineConstructionTest(unittest.TestCase):
    def test_no_notebook_is_extracted_for_none_command(self):
        command = None
        actual = extract_to_be_executed_notebook_from_command_or_none(command)

        self.assertIsNone(actual)

    def test_no_notebook_is_extracted_for_empty_command(self):
        command = ''
        actual = extract_to_be_executed_notebook_from_command_or_none(command)

        self.assertIsNone(actual)

    def test_notebook_is_extracted_for_pyterrier_command(self):
        expected = '/workspace/notebook.ipynb'
        command = '/workspace/run-pyterrier-notebook.py --input $inputDataset --output $outputDir --notebook /workspace/notebook.ipynb'

        actual = extract_to_be_executed_notebook_from_command_or_none(command)

        self.assertEqual(expected, actual)

    def test_notebook_is_extracted_for_command_in_between(self):
        expected = '/notebook.ipynb'
        command = '/workspace/run-notebook.py --notebook /notebook.ipynb --input $inputDataset --output $outputDir'

        actual = extract_to_be_executed_notebook_from_command_or_none(command)

        self.assertEqual(expected, actual)

    def test_no_previous_stages_are_extracted_from_notebook_without_previous_stages(self):
        notebook = TEST_DIR / 'resources' / 'pyterrier-notebook-without-previous-stages.ipynb'
        expected = []

        actual = extract_previous_stages_from_notebook(notebook)

        self.assertEqual(expected, actual)

    def test_pyterrier_index_as_previous_stage(self):
        notebook = TEST_DIR / 'resources' / 'retrieve-with-pyterrier-index.ipynb'
        expected = ['ir-benchmarks/tira-ir-starter/Index (tira-ir-starter-pyterrier)']

        actual = extract_previous_stages_from_notebook(notebook)

        self.assertEqual(expected, actual)

    def test_parsing_of_ast_assignment_none(self):
        python_line = None
        k, v =  parse_ast_extract_assignment(python_line)

        self.assertIsNone(k)
        self.assertIsNone(v)

    def test_parsing_of_ast_assignment_empty_string(self):
        python_line = None
        k, v =  parse_ast_extract_assignment(python_line)

        self.assertIsNone(k)
        self.assertIsNone(v)

    def test_parsing_of_ast_assignment_method_call(self):
        python_line = "index = tira.pt.index('ir-benchmarks/tira-ir-starter/Index (tira-ir-starter-pyterrier)', 'longeval-tiny-train-20240315-training')"
        k, v =  parse_ast_extract_assignment(python_line)

        self.assertIsNone(k)
        self.assertIsNone(v)

    def test_parsing_of_ast_assignment_to_constant(self):
        python_line = "index = 3"
        expected_k, expeced_v = 'index', 3
        k, v =  parse_ast_extract_assignment(python_line)

        self.assertEqual(expected_k, k)
        self.assertEqual(expeced_v, v)

    def test_extraction_of_approach_is_failsave_01(self):
        python_line = "index = None"
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertIsNone(actual)

    def test_extraction_of_approach_is_failsave_02(self):
        python_line = ""
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertIsNone(actual)

    def test_extraction_of_approach_is_failsave_03(self):
        python_line = None
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertIsNone(actual)

    def test_extraction_of_approach_is_failsave_04(self):
        python_line = "#index = tira.pt.index('tmp', 'longeval-tiny-train-20240315-training') # some comment"
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertIsNone(actual)

    def test_extraction_of_approach_01(self):
        python_line = "index = tira.pt.index('ir-benchmarks/tira-ir-starter/Index (tira-ir-starter-pyterrier)', 'longeval-tiny-train-20240315-training')"
        expected = 'ir-benchmarks/tira-ir-starter/Index (tira-ir-starter-pyterrier)'
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertEqual(expected, actual)

    def test_extraction_of_approach_02(self):
        python_line = "index = tira.pt.index('tmp', 'longeval-tiny-train-20240315-training') # some comment"
        expected = 'tmp'
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertEqual(expected, actual)

    def test_extraction_of_approach_03(self):
        python_line = 'index = tira.pt.index("tmp\'\\"a","longeval-tiny-train-20240315-training") # some comment'
        expected = 'tmp\'"a'
        actual =  parse_extraction_of_tira_approach(python_line)

        self.assertEqual(expected, actual)

    def test_integration_against_docker_image_01(self):
        image = 'mam10eks/bash-with-notebooks:latest'
        command = 'bash /workspace/run-notebook.sh --notebook /pyterrier-notebook-without-previous-stages.ipynb --input $inputDataset --output $outputDir'

        expected = []
        actual = extract_previous_stages_from_docker_image(image, command)

        self.assertEqual(expected, actual)

    def test_integration_against_docker_image_02(self):
        image = 'mam10eks/bash-with-notebooks:latest'
        command = 'bash /workspace/run-notebook.sh  --input $inputDataset --output $outputDir --notebook /pyterrier-notebook-without-previous-stages.ipynb'

        expected = []
        actual = extract_previous_stages_from_docker_image(image, command)

        self.assertEqual(expected, actual)


    def test_integration_against_docker_image_03(self):
        image = 'mam10eks/bash-with-notebooks:latest'
        command = 'bash /workspace/run-notebook.sh  --input $inputDataset --output $outputDir --notebook /retrieve-with-pyterrier-index.ipynb'

        expected = ['ir-benchmarks/tira-ir-starter/Index (tira-ir-starter-pyterrier)']
        actual = extract_previous_stages_from_docker_image(image, command)

        self.assertEqual(expected, actual)