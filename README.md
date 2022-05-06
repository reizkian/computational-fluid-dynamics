# Finite Difference Two Dimensional Navier Stokes arround Circular Object

Quick overview of the project can be oppened at [Google Colab](https://colab.research.google.com/drive/1jjYIPgRl4ipRyhntGpk8KwNoPDut_tQ_#scrollTo=RIu-1Je1Hcux).

The numerical solution of the Navier-Stokes equation has been succeeding acquired by finite difference method. The discussion in this simulation involving: how fluid particle movement affect each other, and how the fluid interacts with the geometry of an object and the wall of a channel. There are a consistent physical phenomenon that can be observed such as: Pressure diffusion,Fluid particles compression and Fluid particles dragging effect near the object,finally increases velocity due to the consequence of continuity equation.

## Navier - Stokes Equation
The Navier-Stokes equation which serves as a governing equation is presented in momentum formulation for a viscous incompressible fluid. 
The fluid-solid interaction itself is imposed by the no-slip boundary condition. 

$$
\frac{d \vec{V}}{dt} =
-\frac{1}{\rho} \nabla P(x,y) + \nu \nabla^{2} \vec{V}
$$ 


Broken down into it's dimentional component, The NS equation become:

$$
\begin{split}
\frac{\partial u}{\partial t} +
u \frac{\partial u}{\partial x} + v \frac{\partial u}{\partial y} = 
-\frac{1}{\rho} \frac{\partial P}{\partial x} + 
\nu 
\bigg(
\frac{\partial^{2} u}{\partial x^{2}} + \frac{\partial^{2} u}{\partial y^{2}}
\bigg)
\\
\\
\frac{\partial v}{\partial t} +
u \frac{\partial v}{\partial x} + v \frac{\partial v}{\partial y} = 
-\frac{1}{\rho} \frac{\partial P}{\partial y} + 
\nu 
\bigg(
\frac{\partial^{2} v}{\partial x^{2}} + \frac{\partial^{2} v}{\partial y^{2}}
\bigg)
\\
\\
\frac{\partial^{2} P}{\partial x^{2}}+\frac{\partial^{2} P}{\partial y^{2}} = 
-\rho \bigg[\bigg(\frac{\partial u}{\partial x}\bigg)^2 +
2 \frac{\partial u}{\partial y} \frac{\partial v}{\partial x} +
\bigg(\frac{\partial v}{\partial y}\bigg)^2\bigg]
\end{split}
$$ 


The Navier-Stokes is a system of differential equations which will be directly discretized using finite difference scheme. 
$$
u^{n+1}_{i,j} = u^{n}_{i,j} + \Delta t\Bigg[-u^{n}_{i,j}\bigg(\frac{u^{n}_{i,j}-u^{n}_{i-1,j}}{\Delta x}\bigg)-v^{n}_{i,j}\bigg(\frac{u^{n}_{i,j}-u^{n}_{i,j-1}}{\Delta y} \bigg)-\frac{1}{\rho}\bigg(\frac{P^{n}_{i+1,j}-P^{n}_{i+1,j}}{2\Delta x}\bigg)+\nu \bigg(\frac{u^{n}_{i+1,j}-2u^{n}_{i,j}+u^{n}_{i-1,j}}{\Delta x^{2}}+\frac{u^{n}_{i,j+1}-2u^{n}_{i,j}+u^{n}_{i,j-1}}{\Delta y^{2}}\bigg)\Bigg]
$$ 



$$
v^{n+1}_{i,j} = v^{n}_{i,j} + \Delta t
\Bigg[-u^{n}_{i,j}\bigg(\frac{v^{n}_{i,j}-v^{n}_{i-1,j}}{\Delta x}\bigg)-v^{n}_{i,j}\bigg(\frac{v^{n}_{i,j}-v^{n}_{i,j-1}}{\Delta y} \bigg)-\frac{1}{\rho}\bigg(\frac{P^{n}_{i,j+1}-P^{n}_{i,j-1}}{2\Delta y}\bigg)+\nu\bigg(\frac{v^{n}_{i+1,j}-2v^{n}_{i,j}+v^{n}_{i-1,j}}{\Delta x^{2}}+\frac{v^{n}_{i,j+1}-2v^{n}_{i,j}+v^{n}_{i,j-1}}{\Delta y^{2}}\bigg)\Bigg]
$$ 


$$
P_{i,j} = 
\frac{1}
{2(\Delta x^{2}+\Delta y^{2})} \bigg[\Delta y^{2}(P_{i+1,j}+P_{i-1,j})+
\Delta x^{2}(P_{i,j+1}+P_{i,j-1})-b_{i,j}\Delta x^{2}\Delta y^{2}\bigg]   
 $$

The term $b_{i,j}$ is the source term in discrete manner since the pressure term is to be represented as Poisson equation.

$$
	\frac{\partial^{2} P}{\partial x^{2}}+\frac{\partial^{2} P}{\partial y^{2}} = b(x,y)
$$

## Object Definition
So far the mathematical formulation that we have been discussed does not involve object's geometry. We introduce a scalar field function $E(x,y)$ to represent the object existence in the spatial domain. The scalar field itself does not modify the Navier-Stokes equation at all, differs with volume penalization  introduced a new function which is directly modify to define the object in the spatial domain. Nevertheless, the scalar field $E(x,y)$ is solely influences the numerical scheme that we apply in each case. For convenience the object which will be studied have a circular geometry. The value of $E(x,y)$ is set equal to 1 if for every $(x,y)$ is inside in the circle and set equal to 0 for every $(x,y)$ outside the the circle as shown in the Fig.  

 When it comes to perform two-dimensional flow simulation it is customary to introduce a space grid with the dimension $N_{i} \times N_{j}$. If an object can be described as a mathematical equation, such as a circle, then we must transform the equation from continuous domain $\mathbb{R}^{2}$ into a discrete form. All the variable which specify the geometry of a circle, such as radius $r$ and center position ($a,b$), also under the continuous-discrete transformation. As illustrated in the figure below $(Na,Nb)$ and $Nr$ is the center position and radius of circular bodies respectively in discrete formulation.            

![picture](https://drive.google.com/uc?export=view&id=1GJDUCUVGCE8QICNvrvRPcPIjAjCYGzSp)

Once all the parameters are in the discrete form, the simulation program can be designed to specify the value of the scalar field $E_{i,j}$ which can be used to evaluate boundary conditions at any given point near and inside the object at ease. The main drawback of using the scalar field generated in the space grid domain is the dependency of the object's smoothness to the grid size. Clearly, as figure below shows how grid size affect the smoothness of the circular body is inevitable.

![picture](https://drive.google.com/uc?id=128PnCkr6QqB8BiIyZyiOAqdTSZnOSnbI)
