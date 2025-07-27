from abcvoting.preferences import Profile
from abcvoting import abcrules

profile = Profile(num_cand=5)

voters = [ {0,1,2},
           {3},
           {0,1,2,3},
           {0,1,2,4},
           {0,1},
           {4}]

profile.add_voters(voters)
commitee = 3

w = abcrules.compute_pav(profile, commitee) # returns winning candiate set
print(w)
