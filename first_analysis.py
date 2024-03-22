# main website to get more files inside the article :
# https://www.tfd.chalmers.se/~lada/comp_turb_model/assignment_2_re1000/index.html
# this program was edit by moein maharati (github : mtmoein)


import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
plt.rcParams.update({'font.size': 22})

plt.interactive(True)

# ***** read u

data = np.genfromtxt("u_v_time_4nodes_re1000.dat",comments="%")


u1=data[:,0]   #v_1 at point 1
u2=data[:,2]   #v_1 at point 2
u3=data[:,4]   #v_1 at point 3
u4=data[:,6]   #v_1 at point 4

v1=data[:,1]   #w_1 at point 1
v2=data[:,3]   #w_1 at point 2
v3=data[:,5]   #w_1 at point 3
v4=data[:,7]   #w_1 at point 4


# time step
dt=8.177E-04;
t_tot=dt*len(u1)
t = np.linspace(0,t_tot,len(u1))

# %%%%%%%%%%%%%%%% plotting section %%%%%%%%%%%%%%%%%%%%%%%%%%
# plot u
fig1 = plt.figure("Figure 1")

plt.plot(t,u1,'b--')
plt.plot(t,u4,'r-')
plt.xlabel("t")
plt.ylabel("u")

plt.savefig('u_time_python.png')

####################### # zoom
fig2 = plt.figure("Figure 2")
plt.plot(t,u1,'b--')
plt.plot(t,u4,'r-')
plt.xlabel("t")
plt.ylabel("u")

plt.axis([6, 7, -2, 10])

plt.savefig('u_time_zoom_python.png')

# Zoom in on the time history of u at y/δ = 0.014
# create a plot that focuses on the time interval from ( t = 1 ) to ( t = 2 ) 
#and the velocity range from ( u/uτ = 3 ) to ( u/uτ = 21 )
fig3 = plt.figure("Figure 3")
plt.plot(t, u2, 'b-o')
plt.xlabel("t")
plt.ylabel("u/uτ")
plt.title("Time History of u at y/δ = 0.014")
plt.axis([1, 2, 3, 21])

plt.savefig('ut_time_zoom_python.png')


##########################################################################
# Plotting section for u2, u3, u4, v1, v2, v3, v4

# Plot u2
fig_u2 = plt.figure("Figure u2")
plt.plot(t, u2, 'g--')
plt.xlabel("t")
plt.ylabel("u2")
plt.title("Time History of u2")
plt.savefig('u2_time_python.png')

# Plot u3
fig_u3 = plt.figure("Figure u3")
plt.plot(t, u3, 'm--')
plt.xlabel("t")
plt.ylabel("u3")
plt.title("Time History of u3")
plt.savefig('u3_time_python.png')

# Plot u4
fig_u4 = plt.figure("Figure u4")
plt.plot(t, u4, 'c--')
plt.xlabel("t")
plt.ylabel("u4")
plt.title("Time History of u4")
plt.savefig('u4_time_python.png')

# Plot v1
fig_v1 = plt.figure("Figure v1")
plt.plot(t, v1, 'y--')
plt.xlabel("t")
plt.ylabel("v1")
plt.title("Time History of v1")
plt.savefig('v1_time_python.png')

# Plot v2
fig_v2 = plt.figure("Figure v2")
plt.plot(t, v2, 'k--')
plt.xlabel("t")
plt.ylabel("v2")
plt.title("Time History of v2")
plt.savefig('v2_time_python.png')

# Plot v3
fig_v3 = plt.figure("Figure v3")
plt.plot(t, v3, 'r--')
plt.xlabel("t")
plt.ylabel("v3")
plt.title("Time History of v3")
plt.savefig('v3_time_python.png')

# Plot v4
fig_v4 = plt.figure("Figure v4")
plt.plot(t, v4, 'b--')
plt.xlabel("t")
plt.ylabel("v4")
plt.title("Time History of v4")
plt.savefig('v4_time_python.png')
