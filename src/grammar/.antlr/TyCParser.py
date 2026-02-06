# Generated from c:/Users/USER/OneDrive/my files/Year 3/Sem 2/PPL/Assignment/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,495,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,1,0,1,0,1,0,1,0,5,0,
        107,8,0,10,0,12,0,110,9,0,1,0,1,0,1,1,1,1,1,1,3,1,117,8,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,3,2,126,8,2,1,2,1,2,1,2,1,3,3,3,132,8,3,1,
        3,1,3,1,3,3,3,137,8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,145,8,4,10,4,12,
        4,148,9,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,5,7,159,8,7,10,7,12,
        7,162,9,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,
        1,11,1,11,1,11,1,12,1,12,1,12,5,12,183,8,12,10,12,12,12,186,9,12,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,195,8,14,1,15,1,15,1,15,
        5,15,200,8,15,10,15,12,15,203,9,15,1,16,1,16,1,16,5,16,208,8,16,
        10,16,12,16,211,9,16,1,17,1,17,1,17,5,17,216,8,17,10,17,12,17,219,
        9,17,1,18,1,18,1,18,5,18,224,8,18,10,18,12,18,227,9,18,1,19,1,19,
        1,19,5,19,232,8,19,10,19,12,19,235,9,19,1,20,1,20,1,20,5,20,240,
        8,20,10,20,12,20,243,9,20,1,21,1,21,1,21,5,21,248,8,21,10,21,12,
        21,251,9,21,1,22,1,22,1,22,3,22,256,8,22,1,23,1,23,5,23,260,8,23,
        10,23,12,23,263,9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        3,24,274,8,24,1,25,1,25,3,25,278,8,25,1,25,1,25,1,25,1,25,1,25,3,
        25,285,8,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,294,8,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,3,28,305,8,28,1,28,1,28,
        3,28,309,8,28,1,28,1,28,3,28,313,8,28,1,28,1,28,1,28,1,29,1,29,3,
        29,320,8,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,32,3,32,330,8,32,
        1,32,1,32,1,32,1,32,3,32,336,8,32,1,32,3,32,339,8,32,1,33,1,33,1,
        33,1,33,1,33,3,33,346,8,33,1,33,1,33,1,34,1,34,3,34,352,8,34,1,35,
        1,35,1,35,5,35,357,8,35,10,35,12,35,360,9,35,1,36,1,36,3,36,364,
        8,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,5,37,374,8,37,10,37,
        12,37,377,9,37,1,37,1,37,1,38,4,38,382,8,38,11,38,12,38,383,1,38,
        5,38,387,8,38,10,38,12,38,390,9,38,1,38,3,38,393,8,38,1,39,1,39,
        1,39,1,39,1,39,1,39,3,39,401,8,39,1,40,1,40,1,40,1,41,1,41,1,41,
        1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,3,44,
        421,8,44,1,45,1,45,3,45,425,8,45,1,46,1,46,3,46,429,8,46,1,47,1,
        47,1,47,1,47,5,47,435,8,47,10,47,12,47,438,9,47,1,47,1,47,1,47,1,
        47,5,47,444,8,47,10,47,12,47,447,9,47,1,47,1,47,1,47,3,47,452,8,
        47,1,48,1,48,1,48,1,48,5,48,458,8,48,10,48,12,48,461,9,48,1,48,1,
        48,3,48,465,8,48,1,49,1,49,1,49,1,49,1,49,1,49,5,49,473,8,49,10,
        49,12,49,476,9,49,1,49,1,49,3,49,480,8,49,1,50,1,50,1,50,1,50,5,
        50,486,8,50,10,50,12,50,489,9,50,1,50,1,50,3,50,493,8,50,1,50,0,
        0,51,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,
        88,90,92,94,96,98,100,0,6,4,0,9,9,12,12,14,14,19,19,1,0,27,28,1,
        0,29,32,1,0,22,23,1,0,24,26,2,0,20,23,35,35,518,0,108,1,0,0,0,2,
        113,1,0,0,0,4,121,1,0,0,0,6,131,1,0,0,0,8,141,1,0,0,0,10,149,1,0,
        0,0,12,152,1,0,0,0,14,154,1,0,0,0,16,166,1,0,0,0,18,170,1,0,0,0,
        20,173,1,0,0,0,22,176,1,0,0,0,24,179,1,0,0,0,26,187,1,0,0,0,28,194,
        1,0,0,0,30,196,1,0,0,0,32,204,1,0,0,0,34,212,1,0,0,0,36,220,1,0,
        0,0,38,228,1,0,0,0,40,236,1,0,0,0,42,244,1,0,0,0,44,255,1,0,0,0,
        46,257,1,0,0,0,48,273,1,0,0,0,50,284,1,0,0,0,52,286,1,0,0,0,54,295,
        1,0,0,0,56,301,1,0,0,0,58,319,1,0,0,0,60,321,1,0,0,0,62,323,1,0,
        0,0,64,338,1,0,0,0,66,340,1,0,0,0,68,351,1,0,0,0,70,353,1,0,0,0,
        72,361,1,0,0,0,74,367,1,0,0,0,76,381,1,0,0,0,78,400,1,0,0,0,80,402,
        1,0,0,0,82,405,1,0,0,0,84,408,1,0,0,0,86,412,1,0,0,0,88,420,1,0,
        0,0,90,424,1,0,0,0,92,428,1,0,0,0,94,451,1,0,0,0,96,464,1,0,0,0,
        98,479,1,0,0,0,100,492,1,0,0,0,102,107,3,6,3,0,103,107,3,4,2,0,104,
        107,3,2,1,0,105,107,3,14,7,0,106,102,1,0,0,0,106,103,1,0,0,0,106,
        104,1,0,0,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,
        109,1,0,0,0,109,111,1,0,0,0,110,108,1,0,0,0,111,112,5,0,0,1,112,
        1,1,0,0,0,113,114,5,19,0,0,114,116,5,42,0,0,115,117,3,8,4,0,116,
        115,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,43,0,0,119,
        120,3,96,48,0,120,3,1,0,0,0,121,122,5,17,0,0,122,123,5,19,0,0,123,
        125,5,42,0,0,124,126,3,8,4,0,125,124,1,0,0,0,125,126,1,0,0,0,126,
        127,1,0,0,0,127,128,5,43,0,0,128,129,3,100,50,0,129,5,1,0,0,0,130,
        132,3,12,6,0,131,130,1,0,0,0,131,132,1,0,0,0,132,133,1,0,0,0,133,
        134,5,19,0,0,134,136,5,42,0,0,135,137,3,8,4,0,136,135,1,0,0,0,136,
        137,1,0,0,0,137,138,1,0,0,0,138,139,5,43,0,0,139,140,3,94,47,0,140,
        7,1,0,0,0,141,146,3,10,5,0,142,143,5,45,0,0,143,145,3,10,5,0,144,
        142,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,
        9,1,0,0,0,148,146,1,0,0,0,149,150,3,12,6,0,150,151,5,19,0,0,151,
        11,1,0,0,0,152,153,7,0,0,0,153,13,1,0,0,0,154,155,5,15,0,0,155,156,
        5,19,0,0,156,160,5,40,0,0,157,159,3,16,8,0,158,157,1,0,0,0,159,162,
        1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,160,
        1,0,0,0,163,164,5,41,0,0,164,165,5,44,0,0,165,15,1,0,0,0,166,167,
        3,12,6,0,167,168,5,19,0,0,168,169,5,44,0,0,169,17,1,0,0,0,170,171,
        3,66,33,0,171,172,5,44,0,0,172,19,1,0,0,0,173,174,3,64,32,0,174,
        175,5,44,0,0,175,21,1,0,0,0,176,177,3,26,13,0,177,178,5,44,0,0,178,
        23,1,0,0,0,179,184,3,26,13,0,180,181,5,45,0,0,181,183,3,26,13,0,
        182,180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,
        185,25,1,0,0,0,186,184,1,0,0,0,187,188,3,28,14,0,188,27,1,0,0,0,
        189,195,3,32,16,0,190,191,3,30,15,0,191,192,5,36,0,0,192,193,3,28,
        14,0,193,195,1,0,0,0,194,189,1,0,0,0,194,190,1,0,0,0,195,29,1,0,
        0,0,196,201,5,19,0,0,197,198,5,37,0,0,198,200,5,19,0,0,199,197,1,
        0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,31,1,0,
        0,0,203,201,1,0,0,0,204,209,3,34,17,0,205,206,5,33,0,0,206,208,3,
        34,17,0,207,205,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,
        1,0,0,0,210,33,1,0,0,0,211,209,1,0,0,0,212,217,3,36,18,0,213,214,
        5,34,0,0,214,216,3,36,18,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,
        1,0,0,0,217,218,1,0,0,0,218,35,1,0,0,0,219,217,1,0,0,0,220,225,3,
        38,19,0,221,222,7,1,0,0,222,224,3,38,19,0,223,221,1,0,0,0,224,227,
        1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,37,1,0,0,0,227,225,1,
        0,0,0,228,233,3,40,20,0,229,230,7,2,0,0,230,232,3,40,20,0,231,229,
        1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,1,0,0,0,234,39,1,
        0,0,0,235,233,1,0,0,0,236,241,3,42,21,0,237,238,7,3,0,0,238,240,
        3,42,21,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,242,
        1,0,0,0,242,41,1,0,0,0,243,241,1,0,0,0,244,249,3,44,22,0,245,246,
        7,4,0,0,246,248,3,44,22,0,247,245,1,0,0,0,248,251,1,0,0,0,249,247,
        1,0,0,0,249,250,1,0,0,0,250,43,1,0,0,0,251,249,1,0,0,0,252,253,7,
        5,0,0,253,256,3,44,22,0,254,256,3,46,23,0,255,252,1,0,0,0,255,254,
        1,0,0,0,256,45,1,0,0,0,257,261,3,48,24,0,258,260,3,50,25,0,259,258,
        1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,47,1,
        0,0,0,263,261,1,0,0,0,264,274,5,47,0,0,265,274,5,48,0,0,266,274,
        5,49,0,0,267,274,5,19,0,0,268,269,5,42,0,0,269,270,3,26,13,0,270,
        271,5,43,0,0,271,274,1,0,0,0,272,274,3,72,36,0,273,264,1,0,0,0,273,
        265,1,0,0,0,273,266,1,0,0,0,273,267,1,0,0,0,273,268,1,0,0,0,273,
        272,1,0,0,0,274,49,1,0,0,0,275,277,5,42,0,0,276,278,3,24,12,0,277,
        276,1,0,0,0,277,278,1,0,0,0,278,279,1,0,0,0,279,285,5,43,0,0,280,
        281,5,37,0,0,281,285,5,19,0,0,282,285,5,20,0,0,283,285,5,21,0,0,
        284,275,1,0,0,0,284,280,1,0,0,0,284,282,1,0,0,0,284,283,1,0,0,0,
        285,51,1,0,0,0,286,287,5,11,0,0,287,288,5,42,0,0,288,289,3,26,13,
        0,289,290,5,43,0,0,290,293,3,96,48,0,291,292,5,8,0,0,292,294,3,96,
        48,0,293,291,1,0,0,0,293,294,1,0,0,0,294,53,1,0,0,0,295,296,5,18,
        0,0,296,297,5,42,0,0,297,298,3,26,13,0,298,299,5,43,0,0,299,300,
        3,98,49,0,300,55,1,0,0,0,301,302,5,10,0,0,302,304,5,42,0,0,303,305,
        3,58,29,0,304,303,1,0,0,0,304,305,1,0,0,0,305,306,1,0,0,0,306,308,
        5,44,0,0,307,309,3,60,30,0,308,307,1,0,0,0,308,309,1,0,0,0,309,310,
        1,0,0,0,310,312,5,44,0,0,311,313,3,62,31,0,312,311,1,0,0,0,312,313,
        1,0,0,0,313,314,1,0,0,0,314,315,5,43,0,0,315,316,3,98,49,0,316,57,
        1,0,0,0,317,320,3,64,32,0,318,320,3,26,13,0,319,317,1,0,0,0,319,
        318,1,0,0,0,320,59,1,0,0,0,321,322,3,26,13,0,322,61,1,0,0,0,323,
        324,3,26,13,0,324,63,1,0,0,0,325,326,3,12,6,0,326,329,5,19,0,0,327,
        328,5,36,0,0,328,330,3,26,13,0,329,327,1,0,0,0,329,330,1,0,0,0,330,
        339,1,0,0,0,331,332,5,3,0,0,332,335,5,19,0,0,333,334,5,36,0,0,334,
        336,3,26,13,0,335,333,1,0,0,0,335,336,1,0,0,0,336,339,1,0,0,0,337,
        339,3,66,33,0,338,325,1,0,0,0,338,331,1,0,0,0,338,337,1,0,0,0,339,
        65,1,0,0,0,340,341,3,12,6,0,341,342,5,19,0,0,342,343,5,36,0,0,343,
        345,5,40,0,0,344,346,3,24,12,0,345,344,1,0,0,0,345,346,1,0,0,0,346,
        347,1,0,0,0,347,348,5,41,0,0,348,67,1,0,0,0,349,352,3,26,13,0,350,
        352,3,72,36,0,351,349,1,0,0,0,351,350,1,0,0,0,352,69,1,0,0,0,353,
        358,3,68,34,0,354,355,5,45,0,0,355,357,3,68,34,0,356,354,1,0,0,0,
        357,360,1,0,0,0,358,356,1,0,0,0,358,359,1,0,0,0,359,71,1,0,0,0,360,
        358,1,0,0,0,361,363,5,40,0,0,362,364,3,70,35,0,363,362,1,0,0,0,363,
        364,1,0,0,0,364,365,1,0,0,0,365,366,5,41,0,0,366,73,1,0,0,0,367,
        368,5,16,0,0,368,369,5,42,0,0,369,370,3,26,13,0,370,371,5,43,0,0,
        371,375,5,40,0,0,372,374,3,76,38,0,373,372,1,0,0,0,374,377,1,0,0,
        0,375,373,1,0,0,0,375,376,1,0,0,0,376,378,1,0,0,0,377,375,1,0,0,
        0,378,379,5,41,0,0,379,75,1,0,0,0,380,382,3,78,39,0,381,380,1,0,
        0,0,382,383,1,0,0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,388,1,0,
        0,0,385,387,3,90,45,0,386,385,1,0,0,0,387,390,1,0,0,0,388,386,1,
        0,0,0,388,389,1,0,0,0,389,392,1,0,0,0,390,388,1,0,0,0,391,393,3,
        82,41,0,392,391,1,0,0,0,392,393,1,0,0,0,393,77,1,0,0,0,394,395,5,
        5,0,0,395,396,3,26,13,0,396,397,5,46,0,0,397,401,1,0,0,0,398,399,
        5,7,0,0,399,401,5,46,0,0,400,394,1,0,0,0,400,398,1,0,0,0,401,79,
        1,0,0,0,402,403,5,6,0,0,403,404,5,44,0,0,404,81,1,0,0,0,405,406,
        5,4,0,0,406,407,5,44,0,0,407,83,1,0,0,0,408,409,5,13,0,0,409,410,
        3,26,13,0,410,411,5,44,0,0,411,85,1,0,0,0,412,413,5,13,0,0,413,414,
        5,44,0,0,414,87,1,0,0,0,415,421,3,22,11,0,416,421,3,52,26,0,417,
        421,3,54,27,0,418,421,3,56,28,0,419,421,3,74,37,0,420,415,1,0,0,
        0,420,416,1,0,0,0,420,417,1,0,0,0,420,418,1,0,0,0,420,419,1,0,0,
        0,421,89,1,0,0,0,422,425,3,88,44,0,423,425,3,84,42,0,424,422,1,0,
        0,0,424,423,1,0,0,0,425,91,1,0,0,0,426,429,3,88,44,0,427,429,3,86,
        43,0,428,426,1,0,0,0,428,427,1,0,0,0,429,93,1,0,0,0,430,436,5,40,
        0,0,431,435,3,20,10,0,432,435,3,90,45,0,433,435,3,94,47,0,434,431,
        1,0,0,0,434,432,1,0,0,0,434,433,1,0,0,0,435,438,1,0,0,0,436,434,
        1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,436,1,0,0,0,439,445,
        3,84,42,0,440,444,3,20,10,0,441,444,3,90,45,0,442,444,3,94,47,0,
        443,440,1,0,0,0,443,441,1,0,0,0,443,442,1,0,0,0,444,447,1,0,0,0,
        445,443,1,0,0,0,445,446,1,0,0,0,446,448,1,0,0,0,447,445,1,0,0,0,
        448,449,5,41,0,0,449,452,1,0,0,0,450,452,3,90,45,0,451,430,1,0,0,
        0,451,450,1,0,0,0,452,95,1,0,0,0,453,459,5,40,0,0,454,458,3,20,10,
        0,455,458,3,90,45,0,456,458,3,96,48,0,457,454,1,0,0,0,457,455,1,
        0,0,0,457,456,1,0,0,0,458,461,1,0,0,0,459,457,1,0,0,0,459,460,1,
        0,0,0,460,462,1,0,0,0,461,459,1,0,0,0,462,465,5,41,0,0,463,465,3,
        90,45,0,464,453,1,0,0,0,464,463,1,0,0,0,465,97,1,0,0,0,466,474,5,
        40,0,0,467,473,3,20,10,0,468,473,3,90,45,0,469,473,3,82,41,0,470,
        473,3,80,40,0,471,473,3,98,49,0,472,467,1,0,0,0,472,468,1,0,0,0,
        472,469,1,0,0,0,472,470,1,0,0,0,472,471,1,0,0,0,473,476,1,0,0,0,
        474,472,1,0,0,0,474,475,1,0,0,0,475,477,1,0,0,0,476,474,1,0,0,0,
        477,480,5,41,0,0,478,480,3,90,45,0,479,466,1,0,0,0,479,478,1,0,0,
        0,480,99,1,0,0,0,481,487,5,40,0,0,482,486,3,20,10,0,483,486,3,92,
        46,0,484,486,3,100,50,0,485,482,1,0,0,0,485,483,1,0,0,0,485,484,
        1,0,0,0,486,489,1,0,0,0,487,485,1,0,0,0,487,488,1,0,0,0,488,490,
        1,0,0,0,489,487,1,0,0,0,490,493,5,41,0,0,491,493,3,92,46,0,492,481,
        1,0,0,0,492,491,1,0,0,0,493,101,1,0,0,0,56,106,108,116,125,131,136,
        146,160,184,194,201,209,217,225,233,241,249,255,261,273,277,284,
        293,304,308,312,319,329,335,338,345,351,358,363,375,383,388,392,
        400,420,424,428,434,436,443,445,451,457,459,464,472,474,479,485,
        487,492
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'auto'", "'break'", 
                     "'case'", "'continue'", "'default'", "'else'", "'float'", 
                     "'for'", "'if'", "'int'", "'return'", "'string'", "'struct'", 
                     "'switch'", "'void'", "'while'", "<INVALID>", "'++'", 
                     "'--'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<='", "'>='", "'<'", "'>'", "'||'", "'&&'", 
                     "'!'", "'='", "'.'", "'['", "']'", "'{'", "'}'", "'('", 
                     "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "BLOCK_CMT", "LINE_CMT", "AUTO", "BREAK", 
                      "CASE", "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", 
                      "IF", "INT", "RETURN", "STRING", "STRUCT", "SWITCH", 
                      "VOID", "WHILE", "ID", "INC", "DEC", "PLUS", "MINUS", 
                      "MUL", "DIV", "MOD", "EQ", "NEQ", "LE", "GE", "LT", 
                      "GT", "OR", "AND", "NOT", "ASSIGN", "DOT", "LBRACK", 
                      "RBRACK", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                      "SEMI", "COMMA", "COLON", "INT_LIT", "FLOAT_LIT", 
                      "STRING_LIT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_typeInferFuncDecl = 1
    RULE_voidFuncDecl = 2
    RULE_funcDecl = 3
    RULE_paramList = 4
    RULE_param = 5
    RULE_type = 6
    RULE_structDecl = 7
    RULE_structMemberDecl = 8
    RULE_structInit = 9
    RULE_varDecl = 10
    RULE_exprStmt = 11
    RULE_exprList = 12
    RULE_expr = 13
    RULE_assignExpr = 14
    RULE_lvalue = 15
    RULE_logicalOr = 16
    RULE_logicalAnd = 17
    RULE_equality = 18
    RULE_relational = 19
    RULE_additive = 20
    RULE_multiplicative = 21
    RULE_unary = 22
    RULE_postfix = 23
    RULE_primary = 24
    RULE_postfixOp = 25
    RULE_ifStmt = 26
    RULE_whileStmt = 27
    RULE_forStmt = 28
    RULE_forInit = 29
    RULE_forCond = 30
    RULE_forUpdate = 31
    RULE_varDeclNoSemi = 32
    RULE_structInitNoSemi = 33
    RULE_initElem = 34
    RULE_initList = 35
    RULE_structLit = 36
    RULE_switchStmt = 37
    RULE_switchSection = 38
    RULE_caseLabel = 39
    RULE_continueStmt = 40
    RULE_breakStmt = 41
    RULE_returnStmt = 42
    RULE_voidReturnStmt = 43
    RULE_noReturnstmt = 44
    RULE_stmt = 45
    RULE_voidStmt = 46
    RULE_block = 47
    RULE_typeInferBlock = 48
    RULE_loopBlock = 49
    RULE_voidBlock = 50

    ruleNames =  [ "program", "typeInferFuncDecl", "voidFuncDecl", "funcDecl", 
                   "paramList", "param", "type", "structDecl", "structMemberDecl", 
                   "structInit", "varDecl", "exprStmt", "exprList", "expr", 
                   "assignExpr", "lvalue", "logicalOr", "logicalAnd", "equality", 
                   "relational", "additive", "multiplicative", "unary", 
                   "postfix", "primary", "postfixOp", "ifStmt", "whileStmt", 
                   "forStmt", "forInit", "forCond", "forUpdate", "varDeclNoSemi", 
                   "structInitNoSemi", "initElem", "initList", "structLit", 
                   "switchStmt", "switchSection", "caseLabel", "continueStmt", 
                   "breakStmt", "returnStmt", "voidReturnStmt", "noReturnstmt", 
                   "stmt", "voidStmt", "block", "typeInferBlock", "loopBlock", 
                   "voidBlock" ]

    EOF = Token.EOF
    BLOCK_CMT=1
    LINE_CMT=2
    AUTO=3
    BREAK=4
    CASE=5
    CONTINUE=6
    DEFAULT=7
    ELSE=8
    FLOAT=9
    FOR=10
    IF=11
    INT=12
    RETURN=13
    STRING=14
    STRUCT=15
    SWITCH=16
    VOID=17
    WHILE=18
    ID=19
    INC=20
    DEC=21
    PLUS=22
    MINUS=23
    MUL=24
    DIV=25
    MOD=26
    EQ=27
    NEQ=28
    LE=29
    GE=30
    LT=31
    GT=32
    OR=33
    AND=34
    NOT=35
    ASSIGN=36
    DOT=37
    LBRACK=38
    RBRACK=39
    LBRACE=40
    RBRACE=41
    LPAREN=42
    RPAREN=43
    SEMI=44
    COMMA=45
    COLON=46
    INT_LIT=47
    FLOAT_LIT=48
    STRING_LIT=49
    WS=50
    ERROR_CHAR=51
    ILLEGAL_ESCAPE=52
    UNCLOSE_STRING=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.FuncDeclContext,i)


        def voidFuncDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VoidFuncDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.VoidFuncDeclContext,i)


        def typeInferFuncDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.TypeInferFuncDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.TypeInferFuncDeclContext,i)


        def structDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructDeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 709120) != 0):
                self.state = 106
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 102
                    self.funcDecl()
                    pass

                elif la_ == 2:
                    self.state = 103
                    self.voidFuncDecl()
                    pass

                elif la_ == 3:
                    self.state = 104
                    self.typeInferFuncDecl()
                    pass

                elif la_ == 4:
                    self.state = 105
                    self.structDecl()
                    pass


                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 111
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeInferFuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def typeInferBlock(self):
            return self.getTypedRuleContext(TyCParser.TypeInferBlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(TyCParser.ParamListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_typeInferFuncDecl




    def typeInferFuncDecl(self):

        localctx = TyCParser.TypeInferFuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_typeInferFuncDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(TyCParser.ID)
            self.state = 114
            self.match(TyCParser.LPAREN)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 545280) != 0):
                self.state = 115
                self.paramList()


            self.state = 118
            self.match(TyCParser.RPAREN)
            self.state = 119
            self.typeInferBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidFuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def voidBlock(self):
            return self.getTypedRuleContext(TyCParser.VoidBlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(TyCParser.ParamListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_voidFuncDecl




    def voidFuncDecl(self):

        localctx = TyCParser.VoidFuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_voidFuncDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(TyCParser.VOID)
            self.state = 122
            self.match(TyCParser.ID)
            self.state = 123
            self.match(TyCParser.LPAREN)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 545280) != 0):
                self.state = 124
                self.paramList()


            self.state = 127
            self.match(TyCParser.RPAREN)
            self.state = 128
            self.voidBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def paramList(self):
            return self.getTypedRuleContext(TyCParser.ParamListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_funcDecl




    def funcDecl(self):

        localctx = TyCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 130
                self.type_()


            self.state = 133
            self.match(TyCParser.ID)
            self.state = 134
            self.match(TyCParser.LPAREN)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 545280) != 0):
                self.state = 135
                self.paramList()


            self.state = 138
            self.match(TyCParser.RPAREN)
            self.state = 139
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ParamContext)
            else:
                return self.getTypedRuleContext(TyCParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_paramList




    def paramList(self):

        localctx = TyCParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.param()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 142
                self.match(TyCParser.COMMA)
                self.state = 143
                self.param()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param




    def param(self):

        localctx = TyCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.type_()
            self.state = 150
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_type




    def type_(self):

        localctx = TyCParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 545280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def structMemberDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructMemberDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructMemberDeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_structDecl




    def structDecl(self):

        localctx = TyCParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(TyCParser.STRUCT)
            self.state = 155
            self.match(TyCParser.ID)
            self.state = 156
            self.match(TyCParser.LBRACE)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 545280) != 0):
                self.state = 157
                self.structMemberDecl()
                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 163
            self.match(TyCParser.RBRACE)
            self.state = 164
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structMemberDecl




    def structMemberDecl(self):

        localctx = TyCParser.StructMemberDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structMemberDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.type_()
            self.state = 167
            self.match(TyCParser.ID)
            self.state = 168
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structInitNoSemi(self):
            return self.getTypedRuleContext(TyCParser.StructInitNoSemiContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structInit




    def structInit(self):

        localctx = TyCParser.StructInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.structInitNoSemi()
            self.state = 171
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclNoSemi(self):
            return self.getTypedRuleContext(TyCParser.VarDeclNoSemiContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_varDecl




    def varDecl(self):

        localctx = TyCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.varDeclNoSemi()
            self.state = 174
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_exprStmt




    def exprStmt(self):

        localctx = TyCParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.expr()
            self.state = 177
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_exprList




    def exprList(self):

        localctx = TyCParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.expr()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 180
                self.match(TyCParser.COMMA)
                self.state = 181
                self.expr()
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignExpr(self):
            return self.getTypedRuleContext(TyCParser.AssignExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expr




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.assignExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOr(self):
            return self.getTypedRuleContext(TyCParser.LogicalOrContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(TyCParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def assignExpr(self):
            return self.getTypedRuleContext(TyCParser.AssignExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assignExpr




    def assignExpr(self):

        localctx = TyCParser.AssignExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignExpr)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.logicalOr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.lvalue()
                self.state = 191
                self.match(TyCParser.ASSIGN)
                self.state = 192
                self.assignExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DOT)
            else:
                return self.getToken(TyCParser.DOT, i)

        def getRuleIndex(self):
            return TyCParser.RULE_lvalue




    def lvalue(self):

        localctx = TyCParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(TyCParser.ID)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 197
                self.match(TyCParser.DOT)
                self.state = 198
                self.match(TyCParser.ID)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.LogicalAndContext)
            else:
                return self.getTypedRuleContext(TyCParser.LogicalAndContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.OR)
            else:
                return self.getToken(TyCParser.OR, i)

        def getRuleIndex(self):
            return TyCParser.RULE_logicalOr




    def logicalOr(self):

        localctx = TyCParser.LogicalOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_logicalOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.logicalAnd()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==33:
                self.state = 205
                self.match(TyCParser.OR)
                self.state = 206
                self.logicalAnd()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.EqualityContext)
            else:
                return self.getTypedRuleContext(TyCParser.EqualityContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.AND)
            else:
                return self.getToken(TyCParser.AND, i)

        def getRuleIndex(self):
            return TyCParser.RULE_logicalAnd




    def logicalAnd(self):

        localctx = TyCParser.LogicalAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicalAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.equality()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 213
                self.match(TyCParser.AND)
                self.state = 214
                self.equality()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.RelationalContext)
            else:
                return self.getTypedRuleContext(TyCParser.RelationalContext,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.EQ)
            else:
                return self.getToken(TyCParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.NEQ)
            else:
                return self.getToken(TyCParser.NEQ, i)

        def getRuleIndex(self):
            return TyCParser.RULE_equality




    def equality(self):

        localctx = TyCParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.relational()
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.relational()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(TyCParser.AdditiveContext,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LT)
            else:
                return self.getToken(TyCParser.LT, i)

        def LE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LE)
            else:
                return self.getToken(TyCParser.LE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GT)
            else:
                return self.getToken(TyCParser.GT, i)

        def GE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GE)
            else:
                return self.getToken(TyCParser.GE, i)

        def getRuleIndex(self):
            return TyCParser.RULE_relational




    def relational(self):

        localctx = TyCParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.additive()
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0):
                self.state = 229
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 230
                self.additive()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(TyCParser.MultiplicativeContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.PLUS)
            else:
                return self.getToken(TyCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MINUS)
            else:
                return self.getToken(TyCParser.MINUS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_additive




    def additive(self):

        localctx = TyCParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.multiplicative()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.multiplicative()
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.UnaryContext)
            else:
                return self.getTypedRuleContext(TyCParser.UnaryContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MUL)
            else:
                return self.getToken(TyCParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DIV)
            else:
                return self.getToken(TyCParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MOD)
            else:
                return self.getToken(TyCParser.MOD, i)

        def getRuleIndex(self):
            return TyCParser.RULE_multiplicative




    def multiplicative(self):

        localctx = TyCParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.unary()
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0):
                self.state = 245
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.unary()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(TyCParser.UnaryContext,0)


        def PLUS(self):
            return self.getToken(TyCParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(TyCParser.MINUS, 0)

        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)

        def INC(self):
            return self.getToken(TyCParser.INC, 0)

        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)

        def postfix(self):
            return self.getTypedRuleContext(TyCParser.PostfixContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unary




    def unary(self):

        localctx = TyCParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34375467008) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.unary()
                pass
            elif token in [19, 40, 42, 47, 48, 49]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.postfix()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(TyCParser.PrimaryContext,0)


        def postfixOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.PostfixOpContext)
            else:
                return self.getTypedRuleContext(TyCParser.PostfixOpContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_postfix




    def postfix(self):

        localctx = TyCParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.primary()
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4535488610304) != 0):
                self.state = 258
                self.postfixOp()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(TyCParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(TyCParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(TyCParser.STRING_LIT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def structLit(self):
            return self.getTypedRuleContext(TyCParser.StructLitContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_primary




    def primary(self):

        localctx = TyCParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primary)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [47]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                self.match(TyCParser.INT_LIT)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 265
                self.match(TyCParser.FLOAT_LIT)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 3)
                self.state = 266
                self.match(TyCParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.match(TyCParser.ID)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 5)
                self.state = 268
                self.match(TyCParser.LPAREN)
                self.state = 269
                self.expr()
                self.state = 270
                self.match(TyCParser.RPAREN)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 6)
                self.state = 272
                self.structLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def exprList(self):
            return self.getTypedRuleContext(TyCParser.ExprListContext,0)


        def DOT(self):
            return self.getToken(TyCParser.DOT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def INC(self):
            return self.getToken(TyCParser.INC, 0)

        def DEC(self):
            return self.getToken(TyCParser.DEC, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_postfixOp




    def postfixOp(self):

        localctx = TyCParser.PostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_postfixOp)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(TyCParser.LPAREN)
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352617472) != 0):
                    self.state = 276
                    self.exprList()


                self.state = 279
                self.match(TyCParser.RPAREN)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(TyCParser.DOT)
                self.state = 281
                self.match(TyCParser.ID)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.match(TyCParser.INC)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.match(TyCParser.DEC)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def typeInferBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.TypeInferBlockContext)
            else:
                return self.getTypedRuleContext(TyCParser.TypeInferBlockContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifStmt




    def ifStmt(self):

        localctx = TyCParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(TyCParser.IF)
            self.state = 287
            self.match(TyCParser.LPAREN)
            self.state = 288
            self.expr()
            self.state = 289
            self.match(TyCParser.RPAREN)
            self.state = 290
            self.typeInferBlock()
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 291
                self.match(TyCParser.ELSE)
                self.state = 292
                self.typeInferBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def loopBlock(self):
            return self.getTypedRuleContext(TyCParser.LoopBlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whileStmt




    def whileStmt(self):

        localctx = TyCParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(TyCParser.WHILE)
            self.state = 296
            self.match(TyCParser.LPAREN)
            self.state = 297
            self.expr()
            self.state = 298
            self.match(TyCParser.RPAREN)
            self.state = 299
            self.loopBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMI)
            else:
                return self.getToken(TyCParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def loopBlock(self):
            return self.getTypedRuleContext(TyCParser.LoopBlockContext,0)


        def forInit(self):
            return self.getTypedRuleContext(TyCParser.ForInitContext,0)


        def forCond(self):
            return self.getTypedRuleContext(TyCParser.ForCondContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(TyCParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forStmt




    def forStmt(self):

        localctx = TyCParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(TyCParser.FOR)
            self.state = 302
            self.match(TyCParser.LPAREN)
            self.state = 304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352638472) != 0):
                self.state = 303
                self.forInit()


            self.state = 306
            self.match(TyCParser.SEMI)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352617472) != 0):
                self.state = 307
                self.forCond()


            self.state = 310
            self.match(TyCParser.SEMI)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352617472) != 0):
                self.state = 311
                self.forUpdate()


            self.state = 314
            self.match(TyCParser.RPAREN)
            self.state = 315
            self.loopBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclNoSemi(self):
            return self.getTypedRuleContext(TyCParser.VarDeclNoSemiContext,0)


        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forInit




    def forInit(self):

        localctx = TyCParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_forInit)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 317
                self.varDeclNoSemi()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forCond




    def forCond(self):

        localctx = TyCParser.ForCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forCond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forUpdate




    def forUpdate(self):

        localctx = TyCParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclNoSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def structInitNoSemi(self):
            return self.getTypedRuleContext(TyCParser.StructInitNoSemiContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_varDeclNoSemi




    def varDeclNoSemi(self):

        localctx = TyCParser.VarDeclNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_varDeclNoSemi)
        self._la = 0 # Token type
        try:
            self.state = 338
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.type_()
                self.state = 326
                self.match(TyCParser.ID)
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 327
                    self.match(TyCParser.ASSIGN)
                    self.state = 328
                    self.expr()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
                self.match(TyCParser.AUTO)
                self.state = 332
                self.match(TyCParser.ID)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 333
                    self.match(TyCParser.ASSIGN)
                    self.state = 334
                    self.expr()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 337
                self.structInitNoSemi()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitNoSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TyCParser.TypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def exprList(self):
            return self.getTypedRuleContext(TyCParser.ExprListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_structInitNoSemi




    def structInitNoSemi(self):

        localctx = TyCParser.StructInitNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structInitNoSemi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.type_()
            self.state = 341
            self.match(TyCParser.ID)
            self.state = 342
            self.match(TyCParser.ASSIGN)
            self.state = 343
            self.match(TyCParser.LBRACE)
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352617472) != 0):
                self.state = 344
                self.exprList()


            self.state = 347
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def structLit(self):
            return self.getTypedRuleContext(TyCParser.StructLitContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_initElem




    def initElem(self):

        localctx = TyCParser.InitElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_initElem)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.structLit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def initElem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.InitElemContext)
            else:
                return self.getTypedRuleContext(TyCParser.InitElemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_initList




    def initList(self):

        localctx = TyCParser.InitListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_initList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.initElem()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 354
                self.match(TyCParser.COMMA)
                self.state = 355
                self.initElem()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def initList(self):
            return self.getTypedRuleContext(TyCParser.InitListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_structLit




    def structLit(self):

        localctx = TyCParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_structLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(TyCParser.LBRACE)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352617472) != 0):
                self.state = 362
                self.initList()


            self.state = 365
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(TyCParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(TyCParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def switchSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.SwitchSectionContext)
            else:
                return self.getTypedRuleContext(TyCParser.SwitchSectionContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_switchStmt




    def switchStmt(self):

        localctx = TyCParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(TyCParser.SWITCH)
            self.state = 368
            self.match(TyCParser.LPAREN)
            self.state = 369
            self.expr()
            self.state = 370
            self.match(TyCParser.RPAREN)
            self.state = 371
            self.match(TyCParser.LBRACE)
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==7:
                self.state = 372
                self.switchSection()
                self.state = 377
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 378
            self.match(TyCParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseLabel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.CaseLabelContext)
            else:
                return self.getTypedRuleContext(TyCParser.CaseLabelContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def breakStmt(self):
            return self.getTypedRuleContext(TyCParser.BreakStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switchSection




    def switchSection(self):

        localctx = TyCParser.SwitchSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_switchSection)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 380
                    self.caseLabel()

                else:
                    raise NoViableAltException(self)
                self.state = 383 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352956416) != 0):
                self.state = 385
                self.stmt()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 391
                self.breakStmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_caseLabel




    def caseLabel(self):

        localctx = TyCParser.CaseLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_caseLabel)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(TyCParser.CASE)
                self.state = 395
                self.expr()
                self.state = 396
                self.match(TyCParser.COLON)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(TyCParser.DEFAULT)
                self.state = 399
                self.match(TyCParser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continueStmt




    def continueStmt(self):

        localctx = TyCParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(TyCParser.CONTINUE)
            self.state = 403
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakStmt




    def breakStmt(self):

        localctx = TyCParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.match(TyCParser.BREAK)
            self.state = 406
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_returnStmt




    def returnStmt(self):

        localctx = TyCParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(TyCParser.RETURN)
            self.state = 409
            self.expr()
            self.state = 410
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_voidReturnStmt




    def voidReturnStmt(self):

        localctx = TyCParser.VoidReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_voidReturnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(TyCParser.RETURN)
            self.state = 413
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NoReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprStmt(self):
            return self.getTypedRuleContext(TyCParser.ExprStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(TyCParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(TyCParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(TyCParser.ForStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(TyCParser.SwitchStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_noReturnstmt




    def noReturnstmt(self):

        localctx = TyCParser.NoReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_noReturnstmt)
        try:
            self.state = 420
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21, 22, 23, 35, 40, 42, 47, 48, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.exprStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
                self.ifStmt()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 417
                self.whileStmt()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 418
                self.forStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 419
                self.switchStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noReturnstmt(self):
            return self.getTypedRuleContext(TyCParser.NoReturnstmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(TyCParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_stmt)
        try:
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 16, 18, 19, 20, 21, 22, 23, 35, 40, 42, 47, 48, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.noReturnstmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.returnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def noReturnstmt(self):
            return self.getTypedRuleContext(TyCParser.NoReturnstmtContext,0)


        def voidReturnStmt(self):
            return self.getTypedRuleContext(TyCParser.VoidReturnStmtContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_voidStmt




    def voidStmt(self):

        localctx = TyCParser.VoidStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_voidStmt)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 16, 18, 19, 20, 21, 22, 23, 35, 40, 42, 47, 48, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.noReturnstmt()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
                self.voidReturnStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def returnStmt(self):
            return self.getTypedRuleContext(TyCParser.ReturnStmtContext,0)


        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.VarDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.BlockContext)
            else:
                return self.getTypedRuleContext(TyCParser.BlockContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_block




    def block(self):

        localctx = TyCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 430
                self.match(TyCParser.LBRACE)
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 434
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                        if la_ == 1:
                            self.state = 431
                            self.varDecl()
                            pass

                        elif la_ == 2:
                            self.state = 432
                            self.stmt()
                            pass

                        elif la_ == 3:
                            self.state = 433
                            self.block()
                            pass

                 
                    self.state = 438
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

                self.state = 439
                self.returnStmt()
                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352977416) != 0):
                    self.state = 443
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                    if la_ == 1:
                        self.state = 440
                        self.varDecl()
                        pass

                    elif la_ == 2:
                        self.state = 441
                        self.stmt()
                        pass

                    elif la_ == 3:
                        self.state = 442
                        self.block()
                        pass


                    self.state = 447
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 448
                self.match(TyCParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeInferBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.VarDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def typeInferBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.TypeInferBlockContext)
            else:
                return self.getTypedRuleContext(TyCParser.TypeInferBlockContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_typeInferBlock




    def typeInferBlock(self):

        localctx = TyCParser.TypeInferBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_typeInferBlock)
        self._la = 0 # Token type
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(TyCParser.LBRACE)
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352977416) != 0):
                    self.state = 457
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        self.state = 454
                        self.varDecl()
                        pass

                    elif la_ == 2:
                        self.state = 455
                        self.stmt()
                        pass

                    elif la_ == 3:
                        self.state = 456
                        self.typeInferBlock()
                        pass


                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 462
                self.match(TyCParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.VarDeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def breakStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.BreakStmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.BreakStmtContext,i)


        def continueStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ContinueStmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.ContinueStmtContext,i)


        def loopBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.LoopBlockContext)
            else:
                return self.getTypedRuleContext(TyCParser.LoopBlockContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_loopBlock




    def loopBlock(self):

        localctx = TyCParser.LoopBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_loopBlock)
        self._la = 0 # Token type
        try:
            self.state = 479
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(TyCParser.LBRACE)
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352977496) != 0):
                    self.state = 472
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                    if la_ == 1:
                        self.state = 467
                        self.varDecl()
                        pass

                    elif la_ == 2:
                        self.state = 468
                        self.stmt()
                        pass

                    elif la_ == 3:
                        self.state = 469
                        self.breakStmt()
                        pass

                    elif la_ == 4:
                        self.state = 470
                        self.continueStmt()
                        pass

                    elif la_ == 5:
                        self.state = 471
                        self.loopBlock()
                        pass


                    self.state = 476
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 477
                self.match(TyCParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VoidBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(TyCParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(TyCParser.RBRACE, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.VarDeclContext,i)


        def voidStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VoidStmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.VoidStmtContext,i)


        def voidBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.VoidBlockContext)
            else:
                return self.getTypedRuleContext(TyCParser.VoidBlockContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_voidBlock




    def voidBlock(self):

        localctx = TyCParser.VoidBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_voidBlock)
        self._la = 0 # Token type
        try:
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.match(TyCParser.LBRACE)
                self.state = 487
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 990694352977416) != 0):
                    self.state = 485
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                    if la_ == 1:
                        self.state = 482
                        self.varDecl()
                        pass

                    elif la_ == 2:
                        self.state = 483
                        self.voidStmt()
                        pass

                    elif la_ == 3:
                        self.state = 484
                        self.voidBlock()
                        pass


                    self.state = 489
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 490
                self.match(TyCParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.voidStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





