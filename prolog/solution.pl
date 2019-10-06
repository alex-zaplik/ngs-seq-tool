isCorrect([], 0) :- true.
isCorrect(Xs, N) :- length(Xs, N), forall(member(X, Xs), data(X)).

biocheck([], [], R, R).
biocheck([X|Xs], [Cs | Rests], R, [C|Rr]) :- string_chars(X, [C|Cs]), biocheck(Xs, Rests, R, Rr).

good(X) :- member(a, X), !.
good(X) :- member(t, X), member(c, X), !.

checker(Xs) :- forall(member(X, Xs), X == []), !.
checker(X) :- biocheck(X, Seconds, [], R), good(R), checker(Seconds).