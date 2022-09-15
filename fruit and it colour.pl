fruit(1, apple).
fruit(2, pear).
fruit(3, orange).

read_fruit(FruitName) :-
    repeat,
    write('Please select a fruit:'), nl,
    write_fruit_list,
    read(FruitNumber),
    (   fruit(FruitNumber, FruitName)
    ->  write('You selected: '), write(FruitName), nl, !
    ;   write('Not a valid choice, try again...'), nl, fail
    ).

write_fruit_list :-
    fruit(N, Name),
    write(N), write('. '), write(Name), nl,
    fail.
write_fruit_list.
