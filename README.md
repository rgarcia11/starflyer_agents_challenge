# Starflyer Agents Challenge Variation

## (Original) Starflyers Agents Challenge Description
This description was copied from https://uva.onlinejudge.org/, problem 12315, The Starflyer Agents.

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

  * h1 : f(X, g(c)) h2 : f(f(Y ), Z) h3 : f(c, g(Y, d))
  
Observe that h1 and h2 are compatible because the mapping 

  * θ = {X → f(Y), Z → g(c)} satisfies h1θ = h2θ.
  
However, any other pair from h1, h2, and h3 is not compatible.
Therefore, any sequence of hashes containing h1, h2, and h3 is not compatible because there is no mapping θ such that h1θ = h2θ = h3θ.
Detective Myo has just been briefed on the aforementioned security policy.
She strongly believes that the Starflyer infiltrates the droids via software updates without having any knowledge of the security policy.
If her intuition is right, then this is the chance to detect and stop some Starflyer agents.
You have been assigned to Myo’s team: your task is to write an algorithm for determining if a sequence of hashes is compatible or not.

Can you help Detective Myo to uncover the Starflyer agents?

## Variation Description
The variation is in the θ function and the hash orders. Here, the order of elements in the hash does not matter, but only constants can be mapped to constants, variables to variables and functions to functions, given their input is the same in terms of variables and constants.


## Input
The input consists of several test cases. The first line of each test case contains a string name and a natural number n separated by a blank (2 ≤ n ≤ 20, 1 ≤ |name| ≤ 16). Then n lines follow, each containing a hash hi (1 ≤ i ≤ n, 1 ≤ |hi| ≤ 512).
You can suppose that:
    • The name is an alphanumeric text (without blanks) that has a length less than or equal to 16 characters.
    • Each one of the n hashes was built according to the above definition and has a length less than or equal to 512 characters.
    • The variables, constants, and function symbols are formed exclusively from alphabetic characters.
The first character of a variable symbol is an uppercase letter and the first character of a constant or function symbol is a lowercase letter.
The last test case is followed by a line with the text “END 0”.
  Sample input:
    <pre>
        r2d2 3
        f(X,g(c))
        f(f(Y),Z)
        f(c,g(Y,d))
        c3po 2
        f(X,g(c))
        f(f(c),Z)
        PC2 2
        f(f(Y),Z)
        f(c,g(Y,d))
        END 0
    </pre>
    
## Output

For each test case, a line must be printed. If the sequence of hashes h1, . . . , hn is compatible, then print the line
analysis inconclusive on XXX
or if the sequence of hashes h1, . . . , hn is not compatible, then print the line
XXX is a Starflyer agent
where XXX corresponds to name in the test case.

    Sample output:
    <pre>
        r2d2 is a Starflyer agent
        analysis inconclusive on c3po
        PC2 is a Starflyer agent
    </pre>
    
## Solution

This problem was solved in Python. It uses two scripts: Starflyers.py and DroidAnalyzer.py. Starflyers.py uses imports DroidAnalyzer and uses its functions.
The general strategy was using Python's dictionaries because they allow the user to *ignore* the order, as the problem is about having compatibility between hashes.
When a hash is received, a base dictionary is created in the form

```Python
base_dictionary = {
	'constant':2,
	'variable':1,
	'function':{
		'1':{
			'variable':1,
			'function':{
				'1':{
					'variable':1,
					'constant':2
				}
			}
		},
		'2':{
			'variable':2
			}
	}
}
```

Where the values of 'constant' and 'variable' are the number of constants and variables that the hash has, and the value of 'function' is another dictionary with the same structure, containing 'constant', 'variable' and 'function' keys. 'function' keys contain another dictionary with names '1', '2', and so on, and their value is said dictionary.

That way, it is possible to compare two dictionaries if they have the same structure, for example, these two hashes would have the following output after running DroidAnalyzer.create_structure:

<pre>
f(X,g(c))
f(f(c),Z)
</pre>

```Python
create_structure('f(f(c),Z)') = {
	'function': {
		'1': {
			'variable': 1,
			'function': {
				'1': {
					'constant': 1
				}
			}
		}
	}
}

create_structure('f(f(c),Z)') = {
	'function': {
		'1': {
			'variable': 1,
			'function': {
				'1': {
					'constant': 1
				}
			}
		}
	}
}
```

Meaning that their structure is the same, so they are compatible hashes. This droid would be labeled as inconclusive.

These two are not compatible, for example:

<pre>
f(X,g(c))
f(c,g(Y,d))
</pre>

```Python
create_structure('f(f(c),Z)') = {
	'function': {
		'1': {
			'variable': 1,
			'function': {
				'1': {
					'constant': 1
				}
			}
		}
	}
}

create_structure('f(c,g(Y,d))') = {
	'function': {
		'1': {
			'function': {
				'1': {
					'constant': 1,
					'variable': 1
				}
			},
			'constant': 1
		}
	}
}
```

Their structures are clearly different, and so they aren't compatible. This droid would be labeled as a Starflyer agent.


