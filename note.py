fig1 = plt.figure(figsize=(11,7), dpi=100)
# plotting the pressure field as a contour
plt.contourf(x, y, P, alpha=0.5, cmap=cm.jet)  
plt.colorbar()
# plotting the pressure field outlines
plt.contour(x, y, P, cmap=cm.jet)  
# plotting velocity field
plt.quiver(x,y,u,v) 
plt.xlabel('X')
plt.ylabel('Y');

fig2 = plt.figure(figsize=(11, 7), dpi=100)
plt.contourf(x, y, P, alpha=0.5, cmap=cm.jet)
plt.colorbar()
plt.contour(x, y, P, cmap=cm.jet)
plt.streamplot(x, y, u, v)
plt.xlabel('X')
plt.ylabel('Y');