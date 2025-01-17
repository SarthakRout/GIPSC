mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
mkfile_dir := $(dir $(mkfile_path))

export ROOT_PATH := $(mkfile_dir)

all: test_Milestone4

test_Milestone4:
	./bin/tester

test_Milestone3:
	python3 tests/Milestone3/run_tests.py

test_Milestone2:
	python3 tests/Milestone2/test_regex.py

clean:
	@rm -rf tests/**/*.dot tests/**/*.output tests/**/*.pdf tests/**/*.out tests/**/*.debug tests/**/*.symTables tests/**/*.png tests/**/*3ac.txt