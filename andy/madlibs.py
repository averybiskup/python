from random import choice
person = ['Jason', 'Jordan', 'Michael', 'Samuel', 'Jeff']
place = ['San Francisco', 'The park', 'Los Angeles', 'The Moon', 'Mars']
adjective = ['open', 'big', 'small', 'boring', 'cool', 'loud', 'weird']
plural_noun = ['bananas', 'crabs', 'trees', 'houses', 'mountains', 'beaches']
different_place = ['white house', 'park', 'treehouse', 'mountains', 'beach']
action_verb = ['play', 'sing', 'dance', 'run', 'sleep', 'walk']
food = ['peanut butter', 'crab', 'lobster', 'sushi', 'pizza']
action = ['fight', 'cry', 'swing', 'excercise']
noun = ['soup', 'pie', 'ocean', 'sea', 'fruit cup']

same_place = choice(place)

print("""
Last summer, we went for a vacation with {} on a trip to {}.
The weather there is very {}! Northern {} has many
{}, and they make {} there.
Many people also go to the {} to {}. The
people that live there love to eat {}. They also like to {}
in the sun and swim in the {}.

It was a really {} trip!
""".format(
choice(person),
same_place,
choice(adjective),
same_place,
choice(plural_noun),
choice(plural_noun),
choice(different_place),
choice(action_verb),
choice(food),
choice(action),
choice(noun),
choice(adjective)
))
