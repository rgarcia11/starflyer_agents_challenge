"""
Famed investigator Paula Myo, working on behalf of the 2011 established Commonwealth government, is determined to stop the Starflyer from spying.
The Starflyer is a “human-friendly” and powerful alien sentinel intelligence that was found by a space exploration frigate in the Dyson Alpha solar system in year 2285.
It is not clear what the Starflyer’s real intentions are towards the Commonwealth ... so, it is always better to be safe than sorry!!!
The Starflyer has the ability to control technological equipment; it typically infiltrates droids and uses them as agents.
As a matter of fact, droids are carefully identified and tracked in the Commonwealth.
Every droid has a history of software updates and each software update is tagged with a hash.
A hash is a term built recursively from variable, constant, and function symbols as follows:
• any variable and any constant is a hash;
• if each h1, . . . , hk is a hash and f is a function symbol, then f(h1, . . . , hk) is a hash.
As a security measure, a well-kept secret from the general population, the Commonwealth enforces the following policy on droid software updates:
for each droid, the tags of any software updates must be compatible.
Two hashes h1 and h2 are compatible if there is a mapping θ from variables to hashes such that h1θ = h2θ, where h1θ (resp., h2θ) denotes the simultaneous replacement of any occurrence of each variable x in h1 (resp., h2) with the hash θ(x).
A sequence of hashes h1, . . . , hn is compatible if there is θ such that h1θ, . . . , hnθ are all equal.
For example, assume that X, Y, Z are variables, c, d are constants, and f, g are function symbols, and consider the hashes h1, h2, and h3 as follows:
h1 : f(X, g(c)) h2 : f(f(Y ), Z) h3 : f(c, g(Y, d))
Observe that h1 and h2 are compatible because the mapping θ = {X 7→ f(Y ), Z 7→ g(c)} satisfies h1θ = h2θ.
However, any other pair from h1, h2, and h3 is not compatible.
Therefore, any sequence of hashes containing h1, h2, and h3 is not compatible because there is no mapping θ such that h1θ = h2θ = h3θ.
Detective Myo has just been briefed on the aforementioned security policy.
She strongly believes that the Starflyer infiltrates the droids via software updates without having any knowledge of the security policy.
If her intuition is right, then this is the chance to detect and stop some Starflyer agents.
You have been assigned to Myo’s team: your task is to write an algorithm for determining if a sequence of hashes is compatible or not.

Can you help Detective Myo to uncover the Starflyer agents?
"""
import sys
from DroidAnalyzer import *

def reading(suspects):
    """
    The input consists of several test cases. The first line of each test case contains a string name and a natural number n separated by a blank (2 ≤ n ≤ 20, 1 ≤ |name| ≤ 16). Then n lines follow, each containing a hash hi (1 ≤ i ≤ n, 1 ≤ |hi| ≤ 512).
    You can suppose that:
    • The name is an alphanumeric text (without blanks) that has a length less than or equal to 16 characters.
    • Each one of the n hashes was built according to the above definition and has a length less than or equal to 512 characters.
    • The variables, constants, and function symbols are formed exclusively from alphabetic characters.
    The first character of a variable symbol is an uppercase letter and the first character of a constant or function symbol is a lowercase letter.
    The last test case is followed by a line with the text “END 0”.

    Sample input:
        r2d2 3
        f(X,g(c))
        f(f(Y),Z)
        f(c,g(Y,d))
        c3po 2
        f(X,g(c))
        f(f(Y),Z)
        PC2 2
        f(f(Y),Z)
        f(c,g(Y,d))
        END 0

    Parameters:
        suspects. Dictionary, can be empty or can already contain suspects.
    """
    line = ''
    while line != 'END 0':
        line = sys.stdin.readline()
        if line == "END 0":
            break
        line = line.split()
        droid = line[0]
        number_of_hashes = int(line[1])
        if droid == 'END' and number_of_hashes == 0:
            break
        suspects[droid] = []
        for hashi in range(number_of_hashes):
            line = sys.stdin.readline()
            suspects[droid].append(line.strip())
    return suspects



def writing(suspects):
    """
    For each test case, a line must be printed. If the sequence of hashes h1, . . . , hn is compatible, then print the line
    analysis inconclusive on XXX
    or if the sequence of hashes h1, . . . , hn is not compatible, then print the line
    XXX is a Starflyer agent
    where XXX corresponds to name in the test case.

    Sample output:
        r2d2 is a Starflyer agent
        analysis inconclusive on c3po
        PC2 is a Starflyer agent

    Parameters:
        suspects. Dictionary containing suspects and their hashes
    """
    for droid in suspects.keys():
        guilty = analyze_droid(suspects[droid])
        if guilty:
            print('{} is a Starflyer agent'.format(droid))
        else:
            print('analysis inconclusive on {}'.format(droid))

if __name__ == '__main__':
    """
    Creating the suspects dictionary is the only action needed, the rest comes as input
    """
    suspects = {}
    suspects = reading(suspects)
    writing(suspects)
