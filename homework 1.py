############################################################
# CIS 521: Homework 1
############################################################

student_name = "Jingjing Bai"

# This is where your grade report will be sent.
student_email = "baijingj@seas.upenn.edu" 

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = '''Strong typing means that the type of a value doesn't change in unexpected ways. A string containing only digits doesn't magically become a number, as may happen in Perl. Every change of type requires an explicit conversion. For example, 1+"1" will return type error.
Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type. boo = 1 boo='abc' '''

python_concepts_question_2 = '''points_to_names = {(0, 0): "home", (1, 2): "school", (-1, 1): "market"} '''

python_concepts_question_3 ='''the second way is better. In python, string is not immutable. The first solution is doing N=number of strings concatenations by creating N objects while the second solution is doing one join operation, inside join function, Cpython figures out the memory needed, then allocate a correctly-sized buffer and then fill in each string'''

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(lst, p, f):
    return [f(x) for x in lst if p(x)]
#test
#print(extract_and_apply([1,2],lambda x:x<2, lambda y: y**2))

def concatenate(seqs):
    return [element for item in seqs for element in concatenate(item)] if type(seqs) in [list, tuple] else list(seqs) if type(seqs) is str else [seqs]

#print(concatenate(["abc", (0, [0])]))

def transpose(matrix):
    return [[ matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
#test
#print(transpose([[1,2],[3,4],[5,6]]))
    

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]
#x = [0, 0, 0]; y = copy(x) 
#print(x, y); x[0] = 1; print(x, y) 

def all_but_last(seq):
    return seq[:-1]
#print(all_but_last([]))

def every_other(seq):
    return seq[::2]
#print(every_other([1,2,3,4,5]))
############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    i=0
    while(i <= len(seq)):
        yield seq[:i]
        i+=1

#print(list(prefixes([1,2,3])))

def suffixes(seq):
    i=0
    while(i <=len(seq)):
        yield seq[i:]
        i+=1

#print(list(suffixes([1,2,3])))
def slices(seq):
    for left in range(len(seq)):
        for right in range(left+1,len(seq)+1):
            yield seq[left:right]
#print(list(slices([1,2,3])))
############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join([word.lower() for word in text.strip().split()])

def no_vowels(text):
    return ''.join([x for x in text if x.lower() not in ['a', 'e','i','o','u']])
#print(no_vowels("We love Python!"))

def digits_to_words(text):
    return " ".join([" ".join([{1:"one",0:"zero",2:"two",3:"three",4:"four",5:"five",6:"six", 7:"seven",8:"eight", 9:"nine"}[int(num)] for num in list(word) if num.isdigit()]) for word in text.split() if word.isdigit() or word.replace('.', '', 1).isdigit()])

#print(digits_to_words("Zip Code: 191.04"))
def to_mixed_case(name):
    words = [word.lower() for word in name.replace('_', " ").strip().split()]
    return "".join([words[0]] + [word[0].upper() + word[1:] for word in words[1:]])
#print(to_mixed_case("__Example__NAME"))
    

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.poly = tuple([tuple([coff, level]) for coff, level in polynomial])

    def get_polynomial(self):
        return self.poly

    def __neg__(self):
        return Polynomial(tuple([tuple([-coff, level]) for coff, level in self.poly]))

    def __add__(self, other):
        return Polynomial(self.poly + other.get_polynomial())

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        return Polynomial([ tuple([coff*coff2, level+level2]) for coff, level  in self.poly for coff2, level2  in other.get_polynomial()])

    def __call__(self, x):
        return sum([coff*x**level for coff, level in self.poly ])

    def simplify(self):
        s = [tuple([coff, level]) for coff, level in sorted(self.poly, key=lambda pair:pair[1]) if coff!=0]
        levels = sorted(set(map(lambda x:x[1], s)), reverse=True)
        get_coff_level = lambda level, pair_list:sum([coff for coff,l in s if l==level])
        result = [tuple([get_coff_level(level, s), level]) for level in levels if get_coff_level(level, s)!=0]
        self.poly = tuple(result) if result!=[] else ((0,0),)

    def __str__(self):
        # at least have((0,0),),but double check
        if len(self.poly)==0:
            return ""
        get_mag_part = lambda coff, level: "x^%d"%level if level > 1 else "x" if level ==1 else ""
        get_coff_part = lambda coff, level: {1: " + ", -1: " - "}[coff] if coff in [1, -1] and level!=0 else " + %d"%coff if coff>=0 else " - %d"%-coff
        result = "".join("".join([get_coff_part(coff,level) + get_mag_part(coff, level) for coff, level in self.poly[:1]]).split())
        result += "".join([get_coff_part(coff,level) + get_mag_part(coff, level) for coff, level in self.poly[1:]] )
        return result[1:] if result.startswith("+") else result
        

############################################################
# Section 7: Python Packages
############################################################
import numpy
def sort_array(list_of_matrices):
	return sorted([item for matrix in list_of_matrices for item in list(matrix.flat)], reverse=True)

import nltk
nltk.download('stopwords') 
nltk.download('punkt') 
nltk.download('averaged_perceptron_tagger') 
def POS_tag(sentence):
    from nltk.corpus import stopwords
    from nltk import RegexpParser
    stop_words = set(stopwords.words('english'))
    lower = " ".join([word.lower() for word in sentence.strip().split()])
    #print(lower)
    tokens = nltk.word_tokenize(lower)
    #print(tokens)
    remove = [word for word in tokens if word not in stop_words]
    #print(remove)
    from nltk import pos_tag
    tokens_tag = pos_tag(remove)
    #print("After Token:",tokens_tag)
    return tokens_tag

print(POS_tag("The Force will be with you. Always."))



	

############################################################
# Section 8: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
