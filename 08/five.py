# Alles Korrekt.

import nltk

text = """
Humanism is a philosophy or a way of thinking about the world. Humanism is a set of ethics or ideas about how people should live and act. People who hold this set of ethics are called Humanists.

The most important Humanist ethic is that humans deserve respect. Every human should be treated with respect and allowed to have dignity. If all people act with respect for others, then people will live in peace and trust.
Another important Humanist ethic is that people should all be able to decide how they want to live their lives. The Humanist belief is that if people think hard about what is right and what is wrong, they will know the difference and make right decisions. Thinking asbout problems is called reasoning.
Humanists believe that people should choose what to believe by using reason. The Humanist ethic is that people should not follow any particular religion or philosophy or political belief without first testing it with their own reasoning.
Humanists want to see all humans be as good as they can be. They also want people to be able to achieve the things that they want to do. Humanists decide what choices are good by whether those choices will help make human life better. Whenever there is a problem with our world or our society, humanists think that it is important to use reason to help fix that problem.
"""

tokens = nltk.word_tokenize(text)

for w, t in nltk.pos_tag(tokens):
	print('%s \t\t %s' % (w, t))

# Humanism 		 NNP
# is 		 VBZ
# a 		 DT
# philosophy 		 NN
# or 		 CC
# a 		 DT
# way 		 NN
# of 		 IN
# thinking 		 VBG
# about 		 IN
# the 		 DT
# world 		 NN
# . 		 .
# Humanism 		 NNP
# is 		 VBZ
# a 		 DT
# set 		 NN
# of 		 IN
# ethics 		 NNS
# or 		 CC
# ideas 		 NNS
# about 		 IN
# how 		 WRB
# people 		 NNS
# should 		 MD
# live 		 VB
# and 		 CC
# act 		 VB
# . 		 .
# People 		 NNP
# who 		 WP
# hold 		 NN
# this 		 DT
# set 		 NN
# of 		 IN
# ethics 		 NNS
# are 		 VBP
# called 		 VBN
# Humanists 		 NNS
# . 		 .
# The 		 DT
# most 		 RBS
# important 		 JJ
# Humanist 		 NNP
# ethic 		 JJ
# is 		 VBZ
# that 		 IN
# humans 		 NNS
# deserve 		 VBP
# respect 		 NN
# . 		 .
# Every 		 NNP
# human 		 NN
# should 		 MD
# be 		 VB
# treated 		 VBN
# with 		 IN
# respect 		 NN
# and 		 CC
# allowed 		 VBD
# to 		 TO
# have 		 VB
# dignity 		 NN
# . 		 .
# If 		 IN
# all 		 DT
# people 		 NNS
# act 		 VBP
# with 		 IN
# respect 		 NN
# for 		 IN
# others 		 NNS
# , 		 ,
# then 		 RB
# people 		 NNS
# will 		 MD
# live 		 VB
# in 		 IN
# peace 		 NN
# and 		 CC
# trust 		 NN
# . 		 .
# Another 		 DT
# important 		 JJ
# Humanist 		 NNP
# ethic 		 JJ
# is 		 VBZ
# that 		 IN
# people 		 NNS
# should 		 MD
# all 		 DT
# be 		 VB
# able 		 JJ
# to 		 TO
# decide 		 VB
# how 		 WRB
# they 		 PRP
# want 		 VBP
# to 		 TO
# live 		 VB
# their 		 PRP$
# lives 		 NNS
# . 		 .
# The 		 DT
# Humanist 		 NNP
# belief 		 NN
# is 		 VBZ
# that 		 IN
# if 		 IN
# people 		 NNS
# think 		 VBP
# hard 		 JJ
# about 		 IN
# what 		 WP
# is 		 VBZ
# right 		 RB
# and 		 CC
# what 		 WP
# is 		 VBZ
# wrong 		 JJ
# , 		 ,
# they 		 PRP
# will 		 MD
# know 		 VB
# the 		 DT
# difference 		 NN
# and 		 CC
# make 		 VB
# right 		 RB
# decisions 		 NNS
# . 		 .
# Thinking 		 VBG
# asbout 		 IN
# problems 		 NNS
# is 		 VBZ
# called 		 VBN
# reasoning 		 VBG
# . 		 .
# Humanists 		 NNS
# believe 		 VBP
# that 		 IN
# people 		 NNS
# should 		 MD
# choose 		 VB
# what 		 WP
# to 		 TO
# believe 		 VB
# by 		 IN
# using 		 VBG
# reason 		 NN
# . 		 .
# The 		 DT
# Humanist 		 NNP
# ethic 		 JJ
# is 		 VBZ
# that 		 IN
# people 		 NNS
# should 		 MD
# not 		 RB
# follow 		 VB
# any 		 DT
# particular 		 JJ
# religion 		 NN
# or 		 CC
# philosophy 		 NN
# or 		 CC
# political 		 JJ
# belief 		 NN
# without 		 IN
# first 		 JJ
# testing 		 NN
# it 		 PRP
# with 		 IN
# their 		 PRP$
# own 		 JJ
# reasoning 		 NN
# . 		 .
# Humanists 		 NNS
# want 		 VBP
# to 		 TO
# see 		 VB
# all 		 PDT
# humans 		 NNS
# be 		 VB
# as 		 RB
# good 		 JJ
# as 		 IN
# they 		 PRP
# can 		 MD
# be 		 VB
# . 		 .
# They 		 PRP
# also 		 RB
# want 		 VBP
# people 		 NNS
# to 		 TO
# be 		 VB
# able 		 JJ
# to 		 TO
# achieve 		 VB
# the 		 DT
# things 		 NNS
# that 		 IN
# they 		 PRP
# want 		 VBP
# to 		 TO
# do 		 VB
# . 		 .
# Humanists 		 NNS
# decide 		 VBP
# what 		 WP
# choices 		 NNS
# are 		 VBP
# good 		 JJ
# by 		 IN
# whether 		 IN
# those 		 DT
# choices 		 NNS
# will 		 MD
# help 		 VB
# make 		 VB
# human 		 JJ
# life 		 NN
# better 		 RBR
# . 		 .
# Whenever 		 NNP
# there 		 RB
# is 		 VBZ
# a 		 DT
# problem 		 NN
# with 		 IN
# our 		 PRP$
# world 		 NN
# or 		 CC
# our 		 PRP$
# society 		 NN
# , 		 ,
# humanists 		 NNS
# think 		 VBP
# that 		 IN
# it 		 PRP
# is 		 VBZ
# important 		 JJ
# to 		 TO
# use 		 VB
# reason 		 NN
# to 		 TO
# help 		 VB
# fix 		 CD
# that 		 WDT
# problem 		 NN
# . 	