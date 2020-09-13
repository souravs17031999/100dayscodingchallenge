# Program for solving cryptoarithmetic puzzle where the Input consists of some combinations of
# alphabets and we need to verify the given equation by substituting some number (0-9) assigned to
# all alphabets uniquely to them and none of them can be same.
# SEND
# + MORE
# --------
#  MONEY
# --------
# --------------------------------------------------------------------------------------------------------
# We will use backtracking to solve this problem and try every combinations of digits possible.
bool ExhaustiveSolve(puzzleT puzzle, string lettersToAssign)
{
    if (lettersToAssign.empty()) // no more choices to make
        return PuzzleSolved(puzzle); // checks arithmetic to see if works
    for (int digit = 0; digit <= 9; digit++)   // try all digits
    {
        if (AssignLetterToDigit(lettersToAssign[0], digit))
        {
            if (ExhaustiveSolve(puzzle, lettersToAssign.substr(1)))
                return true;
            UnassignLetterFromDigit(lettersToAssign[0], digit);
        }
    }
    return false;  // nothing worked, need to backtrack
} 
