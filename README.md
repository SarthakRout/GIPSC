# GIPSC
## CS335 Compilers Course Project

We build a compiler from Golang to MIPS using Python. 

## Advanced Features Supported
- Constant Folding
- Multi-dimensional Arrays
- Multilevel pointers
- Custom module imports
- Multiple returns
- Multiple assignments
- Floating point ops
- Goto for labelled statements

## Execution
- Run following command from root directory to run the compiler on a Go source file.
```bash
python src/Milestone6/compiler.py PATH_TO_FILE
```

## [Milestone4](src/Milestone4/)

### Execution
- Run following command from root directory to generate AST for a Go file.
```bash
./bin/parser PATH_TO_FILE
```

### Testing
- To run all the test cases for Milestone 4, run the following command from root of the project : 
```bash
make 
```

## [Milestone3](src/Milestone3/)

### Execution
- Run following command from root directory to run parser on a Go file.
```bash
python src/Milestone3/parser.py PATH_TO_FILE
```

- Run following command from root directory to run lexer on a Go file.
```bash
python src/Milestone3/lexer.py PATH_TO_FILE
```

### Testing
- To run all the test cases for Milestone 3, run the following command from root of the project : 
```bash
make 
```

- To clean generated file run:
```bash
make clean
```

### Visualization
- To obtain dot file, run following commnd from `PROJECT_ROOT/src/Milestone3`:
```bash
python gen_automation.py
```

- To obtain automata, run following command from `PROJECT_ROOT/src/Milestone3`:
```bash
dot -Tpdf test.dot -o automaton.pdf
```

- To obtain parse tree From project root directory, use
```bash
./bin/parser tests/Milestone3/ctest1.go
```

## [Milestone2](src/Milestone2)

### To test regex for tokens
- From project root directory, use 
```python
python3 tests/Milestone2/test_regex.py 
```
or 

```python
make test_Milestone2
```
### To test source code for any program

- Run
```python
python3 src/Milestone2/lexer.py PATH-TO-SOURCE-CODE
```

## SIT Details

Source Language : GoLang
Implementation Language : Python
Target Language : MIPS

## Group Members
- Aditi Goyal
- Devanshu Singla
- Sarthak Rout
- Yatharth Goswami
