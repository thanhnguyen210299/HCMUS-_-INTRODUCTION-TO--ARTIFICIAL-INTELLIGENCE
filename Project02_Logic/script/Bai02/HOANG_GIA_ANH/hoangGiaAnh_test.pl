%Xu ly ket qua trung nhau: setof
%http://www.cse.unsw.edu.au/~billw/dictionaries/prolog/setof.html

%load KB
:- [hoangGiaAnh].

:- writeln('Cau 1: Ai la chong cua Diana Pricess of Wales ?').
:- writeln('Cau 2: Ai la vo cu Prince Phillip ?').
:- writeln('Cau 3: Ai la cha cua Princess Beatrice of York ?').
:- writeln('Cau 4: Ai la me cua Prince Charles ?').
:- writeln('Cau 5: Ai la con cua Prince Edward ?').
:- writeln('Cau 6: Ai la con trai cua Princess Anne ?').
:- writeln('Cau 7: Ai la con gai cua Kate Middleton ?').
:- writeln('Cau 8: Ai la ong/ba cua Archie Harrison Mountbatten-Windsor ?').
:- writeln('Cau 9: Ai la ba cua Zara Tindall ?').
:- writeln('Cau 10: Ai la ong cua Pricess Eugenie ?').
:- writeln('Cau 11: Ai la chau cua Queen Elizabeth II ?').
:- writeln('Cau 12: Ai la chay trai cua Prince Phillip ?').
:- writeln('Cau 13: Ai la chau gai cua Prince Charles ?').
:- writeln('Cau 14: Ai la anh/chi/em ruot cua Prince George ?').
:- writeln('Cau 15: Ai la anh/em trai cua Lady Louise Windsor ?').
:- writeln('Cau 16: Ai la chi/em gai cua Peter Phillips ?').
:- writeln('Cau 17: Ai la di cua Prince William ?').
:- writeln('Cau 18: Ai la cau cua James, Viscount Severn?').
:- writeln('Cau 19: Ai la chau gai cua Sarah Ferguson ?').
:- writeln('Cau 20: Ai la chau trai cua Camilla Parker Bowles ?').
:- writeln(' ').
:- writeln('Press cau_1, cau_2, cau_3,..., cau_20 to see question and answer.').




cau_1 :- 
	writeln('Ai la chong cua Diana Pricess of Wales ?'),
	husband(Person, princess_diana) -> writeln(Person); writeln('Khong biet').

cau_2 :- 
	writeln('Ai la vo cu Prince Phillip ?'),
	wife(Person, prince_philip) -> writeln(Person); writeln('Khong biet').

cau_3 :- 
	writeln('Ai la cha cua Princess Beatrice of York ?'),		
	father(Person, princess_beatrice) -> writeln(Person); writeln('Khong biet').

cau_4 :-
	writeln('Ai la me cua Prince Charles'),
	mother(Person, prince_charles) -> writeln(Person); writeln('Khong biet').

cau_5 :-
	writeln('Ai la con cua Prince Edward ?'),
	setof(Child, child(Child, prince_edward), List),
	writeln(List).

cau_6 :-
	writeln('Ai la con trai cua Princess Anne ?'),
	setof(Child, son(Child, princess_anne), List),
	writeln(List).

cau_7 :-
	writeln('Ai la con gai cua Kate Middleton ?'),
	setof(Child, daughter(Child, kate_middleton), List),
	writeln(List).

cau_8 :-
	writeln('Ai la ong/ba cua Archie Harrison Mountbatten-Windsor ?'),
	setof(GP, grandparent(GP, archie_harrison), List),
	writeln(List).

cau_9 :-
	writeln('Ai la ba cua Zara Tindall ?'),
	setof(GM, grandmother(GM, zara_tindall), List),
	writeln(List).

cau_10 :-
	writeln('Ai la ong cua Pricess Eugenie ?'),
	setof(GF, grandfather(GF, princess_eugenie), List),
	writeln(List).

cau_11 :-
	writeln('Ai la chau cua Queen Elizabeth II ?'),
	setof(GC, grandchild(GC, queen_elizabeth_II), List),
	writeln(List).

cau_12 :-
	writeln('Ai la chay trai cua Prince Phillip ?'),
	setof(GS, grandson(GS, prince_philip) ,List),
	writeln(List).

cau_13 :-
	writeln('Ai la chau gai cua Prince Charles ?'),
	setof(GD, granddaughter(GD, prince_charles), List),
	writeln(List).

cau_14 :-
	writeln('Ai la anh/chi/em ruot cua Prince George ?'),
	setof(Person, sibling(Person, prince_george), List),
	writeln(List).

cau_15 :-
	writeln('Ai la anh/em trai cua Lady Louise Windsor ?'),
	setof(Person, brother(Person, lady_loulse), List),
	writeln(List).

cau_16 :-
	writeln('Ai la chi/em gai cua Peter Phillips ?'),
	setof(Person, sister(Person, peter_phillips), List),
	writeln(List).

cau_17 :-
	writeln('Ai la di cua Prince William ?'),
	setof(Person, aunt(Person, prince_william), List),
	writeln(List).

cau_18 :-
	writeln('Ai la cau cua James, Viscount Severn?'),
	setof(Person, uncle(Person, james_severn), List),
	writeln(List).

cau_19 :-
	writeln('Ai la chau gai cua Sarah Ferguson ?'),
	setof(Person, niece(Person, sarah_ferguson), List),
	writeln(List).

cau_20 :-
	writeln('Ai la chau trai cua Camilla Parker Bowles ?'),
	setof(Person, nephew(Person, camilla_bowles), List),
	writeln(List).
