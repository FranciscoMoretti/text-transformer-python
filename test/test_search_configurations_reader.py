import json
from pathlib import Path
from test.sample_resources import PATTERN_LIST_SAMPLE, PATTERNS_SAMPLE
from test.utils.tmp_path import _get_tmp_path_to_file

from src.search_configuration import SearchConfiguration
from src.search_configurations_reader import SearchConfigurationsReader


def test_from_list_of_dictionaries():
    assert (
        PATTERN_LIST_SAMPLE
        == SearchConfigurationsReader.from_list_of_dictionaries(
            PATTERNS_SAMPLE
        )
    )


def test_from_json_file(tmp_path):
    filepath = _get_tmp_path_to_file(tmp_path)
    filepath.write_text(json.dumps(PATTERNS_SAMPLE))
    assert PATTERN_LIST_SAMPLE == SearchConfigurationsReader.from_json_file(
        filepath
    )


PATH_TO_PATTERNS_SAMPLE_FILE = Path("./test/patterns_sample.json")


def test_read_from_file():
    expected_list = [
        SearchConfiguration(name="foo", regex_pattern='foo="bar"')
    ]
    assert expected_list == SearchConfigurationsReader.from_json_file(
        PATH_TO_PATTERNS_SAMPLE_FILE
    )
