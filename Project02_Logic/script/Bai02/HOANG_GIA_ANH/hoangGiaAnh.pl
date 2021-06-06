%parent(Parent, Child)
parent(prince_philip, prince_charles).
parent(prince_philip, prince_andrew).
parent(prince_philip, princess_anne).
parent(prince_philip, prince_edward).
parent(queen_elizabeth_II, prince_charles).
parent(queen_elizabeth_II, prince_andrew).
parent(queen_elizabeth_II, princess_anne).
parent(queen_elizabeth_II, prince_edward).

parent(prince_charles, prince_william).
parent(prince_charles, prince_harry).
parent(princess_diana, prince_william).
parent(princess_diana, prince_harry).

parent(prince_william, prince_george).
parent(prince_william, princess_charlotte).
parent(prince_william, prince_louis).
parent(kate_middleton, prince_george).
parent(kate_middleton, princess_charlotte).
parent(kate_middleton, prince_louis).

parent(prince_harry, archie_harrison).
parent(meghan_markle, archie_harrison).

parent(prince_andrew, princess_eugenie).
parent(prince_andrew, princess_beatrice).
parent(sarah_ferguson, princess_eugenie).
parent(sarah_ferguson, princess_beatrice).

parent(mark_phillips, peter_phillips).
parent(mark_phillips, zara_tindall).

parent(princess_anne, peter_phillips).
parent(princess_anne, zara_tindall).

parent(prince_edward, lady_loulse).
parent(prince_edward, james_severn).
parent(sophie_rhys_jones, lady_loulse).
parent(sophie_rhys_jones, james_severn).


%male(Person)
male(prince_philip).
male(prince_charles).
male(prince_andrew).
male(prince_william).
male(prince_harry).
male(prince_george).
male(prince_louis).
male(archie_harrison).
male(mark_phillips).
male(timothy_laurence).
male(prince_edward).
male(peter_phillips).
male(mike_tindall).
male(james_severn).


%female(Person)
female(queen_elizabeth_II).
female(princess_diana).
female(camilla_bowles).
female(sarah_ferguson).
female(kate_middleton).
female(meghan_markle).
female(princess_eugenie).
female(princess_beatrice).
female(princess_charlotte).
female(princess_anne).
female(sophie_rhys_jones).
female(autumn_phillips).
female(zara_tindall).
female(lady_loulse).



%married(Person, Person)
married(queen_elizabeth_II, prince_philip).
married(prince_charles, camilla_bowles).
married(kate_middleton, prince_william).
married(prince_harry, meghan_markle).
married(prince_andrew, sarah_ferguson).
married(princess_anne, timothy_laurence).
married(peter_phillips, autumn_phillips).
married(zara_tindall, mike_tindall).
married(prince_edward, sophie_rhys_jones).

married(prince_philip, queen_elizabeth_II).
married(camilla_bowles, prince_charles).
married(prince_william, kate_middleton).
married(meghan_markle, prince_harry).
married(sarah_ferguson, prince_andrew).
married(timothy_laurence, princess_anne).
married(autumn_phillips, peter_phillips).
married(mike_tindall, zara_tindall).
married(sophie_rhys_jones, prince_edward).


%divorced(Person, Person)
divorced(princess_diana, prince_charles).
divorced(mark_phillips, princess_anne).

divorced(prince_charles, princess_diana).
divorced(princess_anne, mark_phillips).




%husband(Person,Wife)
%wife(Person,Husband)
%father(Parent,Child)
%mother(Parent,Child) 
%child(Child,Parent) 
%son(Child,Parent) 
%daughter(Child,Parent)

husband(Person, Wife) :- married(Person, Wife), male(Person).
wife(Person, Husband) :- married(Person, Husband), female(Person).
father(Parent, Child) :- parent(Parent, Child), male(Parent).
mother(Parent, Child) :- parent(Parent, Child), female(Parent).
child(Child, Parent) :- parent(Parent, Child).
son(Child, Parent) :- parent(Parent, Child), male(Child).
daughter(Child, Parent) :- parent(Parent, Child), female(Child).



%grandparent(GP,GC) 
%grandmother(GM,GC) 
%grandfather(GF,GC) 
%grandchild(GC,GP)
%grandson(GS,GP) 
%granddaughter(GD,GP)

grandparent(GP, GC) :- parent(GP, Parent), parent(Parent, GC).
grandmother(GM, GC) :- parent(GM, Parent), parent(Parent, GC), female(GM).
grandfather(GF, GC) :- parent(GF, Parent), parent(Parent, GC), male(GF).
grandchild(GC, GP) :- parent(GP, Parent), parent(Parent, GC).
grandson(GS, GP) :- parent(GP, Parent), parent(Parent, GS), male(GS).
granddaughter(GD, GP) :- parent(GP, Parent), parent(Parent, GD), female(GD).



%sibling(Person1,Person2) 
%brother(Person,Sibling)
%sister(Person,Sibling)
%aunt(Person,NieceNephew)
%uncle(Person,NieceNephew)
%niece(Person,AuntUncle)
%nephew(Person,AuntUncle)

sibling(Person1, Person2) :- parent(Parent, Person1), parent(Parent, Person2), Person1\==Person2.
brother(Person, Sibling) :- sibling(Person, Sibling), male(Person).
sister(Person, Sibling) :- sibling(Person, Sibling), female(Person).
aunt(Person, NieceNephew) :- parent(Parent,NieceNephew),(sister(Person,Parent);(brother(Uncle,Parent),wife(Person,Uncle))).
uncle(Person, NieceNephew) :- parent(Parent,NieceNephew), (brother(Person,Parent);(sister(Aunt,Parent),husband(Person,Aunt))).
niece(Person, AuntUncle) :- (aunt(AuntUncle,Person);uncle(AuntUncle,Person)),female(Person).
nephew(Person, AuntUncle) :- (aunt(AuntUncle,Person);uncle(AuntUncle,Person)),male(Person).

