from typing import Literal
from typeguard import typechecked

class Grade:
    __slots__ = ['__grade', '__weight', '__comment', '__valid', '__invalidation_reason']

    # TODO: Do something so that we got intermediate thingies.
    # TODO: maybe a field for just "plus" ? have to think about it.
    grades = Literal[1, 2, 3, 4, 5, 6]
    weights = Literal[1, 2, 3, 4]
    
    @typechecked
    def __init__(self, grade: grades, weight: weights=1, comment: str=None) -> None:
        
        self.__grade = grade
        self.__weight = weight
        # TODO: dateime automaticaly added to comment while created
        self.__comment = comment
        self.__valid = True
        
    
    def get_grade(self) -> int:
        return self.__grade
    
    def get_weight(self) -> int:
        return self.__weight
    
    def get_comment(self) -> str:
        return self.__comment
    
    def is_valid(self) -> bool:
        return self.__valid
    
    @typechecked
    def change_weight(self, weight: weights) -> None:
        # TODO: Exeception?
        if self.__valid:
            self.__weight = weight
        else:
            print('Grade invalidated. Cannot change.')    
    
    @typechecked
    def add_comment(self, comment: str) -> None:
        # TODO: Exeception?
        if self.__valid:
            # TODO: datetime automaticaly added to edit
            # TODO: change comments section to list
            self.__comment += '; ' + comment
        else:
            print('Grade invalidated. Cannot change.')
            
    @typechecked
    def invalidate(self, reason) -> None:
        # TODO: Exeception?
        if self.__valid:
            self.__valid = False
            self.__invalidation_reason = reason
        else:
            print('Grade invalidated. Cannot change.')
            
    
    def __repr__(self) -> str:        
        message = ''
          
        if not self.__valid:
            message += 'invalidated: ' + self.__invalidation_reason + ', '     
                   
        message += 'grade: ' + str(self.__grade) + ', weight: ' + str(self.__weight)        
        
        if self.__comment:
            message += ', comment: ' + self.__comment       
                 
        return message
            
        
    grade = property(get_grade)
    weight = property(get_weight, change_weight)
    comment = property(get_comment, add_comment)
    valid = property(is_valid)
    