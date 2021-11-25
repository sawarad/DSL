from typing import Tuple, List, Set, Dict, Union
from copy import deepcopy

Class = int
Value = str
Token = Tuple[Class, Value]
Tokens = Set[Token]

Var = str
Rule = List[Union[Var, Token]]
Definition = List[Rule]
Variables = Dict[Var, Definition]


class Grammar:
    def __init__(self, tokens: Tokens, variables: Variables, main_var: Var):
        self.tokens = tokens
        self.variables = variables
        self.main_var = main_var
        assert self.main_var in self.variables

    def __str__(self) -> str:
        return str(self.tokens) + "\n\n" + str(self.variables) + "\n\n" + str(self.main_var)
    
    def __copy__(self):
        return Grammar(
            deepcopy(self.tokens),
            deepcopy(self.variables),
            deepcopy(self.main_var)
        )


def is_token(to_check) -> bool:
    if not isinstance(to_check, Tuple):
        return False
    
    return len(to_check) == 2 and isinstance(to_check[0], Class) and isinstance(to_check[1], Value)


def is_empty_token(to_check) -> bool:
    if not is_token(to_check):
        return False
    
    # assume empty token is a token with class == 0 and empty value
    # can be changed without affecting other code
    return to_check[0] == 0 and to_check[1] == ""


def get_empty_token() -> Token:
    return 0, ""


def is_var(to_check) -> bool:
    return isinstance(to_check, Var)
