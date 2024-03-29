"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]],
            "answer": "DOT",
        },
        {
            "input": [["POP", "POP"]],
            "answer": "",
        },
        {
            "input": [["PUSH H", "PUSH I"]],
            "answer": "HI",
        },
        {
            "input": [[]],
            "answer": "",
        },
    ],
    "Edge": [
        {
            "input": [["POP"]],
            "answer": "",
        },
        {
            "input": [["PUSH Z"]],
            "answer": "Z",
        },
        {
            "input": [['PUSH A', 'PUSH B', 'PUSH C', 'PUSH D', 'PUSH E', 'PUSH F', 'PUSH G', 'PUSH H', 'PUSH I',
                      'PUSH J', 'PUSH K', 'PUSH L', 'PUSH M', 'PUSH N', 'PUSH O', 'PUSH P', 'PUSH Q', 'PUSH R',
                      'PUSH S', 'PUSH T', 'PUSH U', 'PUSH V', 'PUSH W', 'PUSH X', 'PUSH Y', 'PUSH Z']],
            "answer": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        },
        {
            "input": [['PUSH A', 'PUSH B', 'PUSH C', 'PUSH D', "POP", 'PUSH E', 'PUSH F', 'PUSH G', 'PUSH H', "POP", 'PUSH I', 'PUSH J', 'PUSH K', 'PUSH L', "POP", "POP", 'PUSH M', 'PUSH N', 'PUSH O', 'PUSH P', 'PUSH Q', 'PUSH R', 'PUSH S', 'PUSH T', 'PUSH U', 'PUSH V', 'PUSH W', 'PUSH X', 'PUSH Y', 'PUSH Z']],
            "answer": "EFGHIJKLMNOPQRSTUVWXYZ",
        },
    ],
    "Extra": [
        {
            "input": [['PUSH X', 'POP', 'POP', 'POP', 'POP', 'PUSH J', 'PUSH V', 'PUSH J', 'PUSH H', 'POP', 'PUSH H', 'PUSH M', 'POP', 'PUSH K', 'PUSH T']],
            "answer": "JHHMKT"
        },
        {
            "input": [['PUSH C', 'PUSH B']],
            "answer": "CB"
        },
        {
            "input": [['POP', 'PUSH S', 'POP', 'PUSH X', 'PUSH U', 'POP', 'POP', 'PUSH X', 'POP', 'POP', 'PUSH Z', 'PUSH G', 'POP', 'PUSH F', 'PUSH M', 'PUSH I', 'POP', 'POP', 'POP', 'PUSH S', 'POP', 'POP', 'PUSH S', 'PUSH E', 'POP', 'POP', 'PUSH E']],
            "answer": "E"
        },
        {
            "input": [['PUSH U', 'POP', 'PUSH B', 'PUSH O', 'PUSH G', 'POP', 'POP', 'PUSH R', 'POP', 'POP', 'POP', 'PUSH J', 'PUSH N', 'PUSH D', 'PUSH V', 'POP', 'PUSH S', 'POP', 'PUSH P']],
            "answer": "DVSP"
        },
        {
            "input": [['PUSH B', 'PUSH H', 'PUSH H', 'PUSH U', 'PUSH G', 'POP', 'PUSH S', 'POP', 'PUSH O', 'POP', 'PUSH C', 'POP', 'PUSH L', 'PUSH A', 'POP', 'PUSH C']],
            "answer": "SOCLAC"
        },
        {
            "input": [['POP', 'POP', 'PUSH B', 'POP', 'POP', 'PUSH Q', 'PUSH S', 'POP', 'POP', 'POP', 'POP', 'POP', 'PUSH Y', 'PUSH T', 'PUSH P', 'PUSH Y', 'PUSH O', 'PUSH N', 'POP', 'POP', 'PUSH M', 'PUSH U', 'POP', 'PUSH N', 'PUSH P', 'PUSH R', 'PUSH U', 'PUSH J', 'PUSH X']],
            "answer": "YONMUNPRUJX"
        },
    ]
}
