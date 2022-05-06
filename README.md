# Finite Difference Two Dimensional Navier Stokes arround Circular Object

https://colab.research.google.com/drive/1jjYIPgRl4ipRyhntGpk8KwNoPDut_tQ_#scrollTo=RIu-1Je1Hcux

The numerical solution of the Navier-Stokes equation has been succeeding acquired by finite difference method. The discussion in this simulation involving: how fluid particle movement affect each other, and how the fluid interacts with the geometry of an object and the wall of a channel. There are a consistent physical phenomenon that can be observed such as: Pressure diffusion,Fluid particles compression and Fluid particles dragging effect near the object,finally increases velocity due to the consequence of continuity equation.

## Navier - Stokes Equation
The Navier-Stokes equation which serves as a governing equation is presented in momentum formulation for a viscous incompressible fluid. 
The fluid-solid interaction itself is imposed by the no-slip boundary condition. 

```math
\begin{equation*}
\frac{d \vec{V}}{dt} =
-\frac{1}{\rho} \nabla P(x,y) + \nu \nabla^{2} \vec{V}
\end{equation*}
```
