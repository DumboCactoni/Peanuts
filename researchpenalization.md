# Stirrer Shape Paper: Equations in Sections 3.1–3.3

An equation-by-equation explanation of the attached paper. The equations follow the paper as printed. Apparent printing errors and ambiguous notation are noted alongside the affected equations.

## Section 3.1: The cost functional

### Equation 3.1

$$
\mathcal J=\left.\frac{1}{V_\Omega}\int_\Omega\|\nabla^k\theta\|\,d\Omega\right|_T.
$$

**Symbols.** $\mathcal J$ is the mixing score; $\theta$ is the scalar concentration field; $\Omega$ is the domain; $V_\Omega$ is its volume, or area in two dimensions; $d\Omega$ is a small piece of that domain; and $T$ is the final time. The vertical bar means evaluate the expression at $T$. The gradient $\nabla$ is the collection of spatial partial derivatives: $(\partial/\partial x,\partial/\partial y)$ in two dimensions, with $\partial/\partial z$ added in three dimensions. The exponent $k$ is the order of the operator; the paper selects $k=-2/3$.

**Groups of terms.** $\nabla^k\theta$ applies the order-$k$ operator to the concentration field. The integral combines the result across the domain; $1/V_\Omega$ normalizes by domain size.

**Whole equation.** It assigns a final mixing score. The negative order gives greater weight to large-scale concentration differences than to equally strong fine-scale ones. A negative fractional-order operator is not an ordinary first-derivative gradient; the section does not fully specify its construction or zero-frequency treatment.

### Equation 3.2

$$
\mathcal J=\left.\frac{\sqrt{[A^{-2/3}\theta]^H M[A^{-2/3}\theta]}}{V_\Omega}\right|_T.
$$

**Symbols.** $\mathcal J$ is the score; $\theta$ is the scalar represented on the grid; $V_\Omega$ is the domain volume or area; and $T$ is the final time. $A$ is the paper's discrete spatial-differentiation notation; the matrices $A_i$ represent spatial partial derivatives on the grid. $A^{-2/3}$ is its notation for a discrete negative fractional-order operation. $M$ is a grid-weighting matrix. The superscript $H$ means conjugate transpose.

**Groups of terms.** $A^{-2/3}\theta$ transforms the scalar values. The quadratic expression $[A^{-2/3}\theta]^H M[A^{-2/3}\theta]$ combines those values using the grid weights; the square root gives a magnitude. $V_\Omega$ supplies the printed normalization.

**Whole equation.** This is the paper's grid-based expression for the final mixing score. The section does not fully explain how the fractional power of its multidimensional differentiation notation is constructed.

### Equation 3.3

$$
M=\frac{1}{n^2}I.
$$

**Symbols.** $M$ is the weighting matrix in 3.2. $I$ is the identity matrix, with ones on its main diagonal and zeros elsewhere. Here $n^2$ is the number of points in the two-dimensional grid.

**Group of terms.** Multiplying $I$ by $1/n^2$ gives every grid point the same diagonal weight.

**Whole equation.** It defines the weighting matrix used for the equally spaced grid.

## Section 3.2: The adjoint system

### Equation 3.4

$$
\begin{aligned}
\mathcal L=\mathcal J-\int_0^T
&(\mathbf u^\dagger)_k^H M
\left\{\partial_t\mathbf u+u_j\circ[A_j\mathbf u]
+\frac{\chi}{C_\eta}\circ\mathbf u
-\frac{\chi_i}{C_\eta}\circ\mathbf u_{s,i}
+Ap-Re^{-1}[A_iA_i\mathbf u]\right\}_k\\
&+p^{\dagger,H}M\left\{[A_iA_i]p+A_i(u_j\circ[A_ju_i])
+A_i\left[\frac{\chi}{C_\eta}-\frac{\chi_i}{C_\eta}\circ\mathbf u_{s,i}\right]\right\}\\
&+\theta^{\dagger,H}M\left\{\partial_t\theta
+(1-\chi)\circ u_j\circ[A_j\theta]
-\chi\circ(\mathbf u_{s,i})_j\circ[A_j\theta]
-A_i\left([Pe^{-1}(1-\chi)+\kappa\chi]\circ A_i\theta\right)\right\}\\
&+\chi_i^{\dagger,H}M[\chi_i-g_i(\mathbf x,t)]\,dt.
\end{aligned}
$$

**Symbols.** $\mathcal L$ is the augmented cost and $\mathcal J$ is the mixing score. $\mathbf u$, $p$, and $\theta$ are fluid velocity, pressure, and scalar concentration. $\mathbf u_{s,i}$ is the prescribed velocity of stirrer $i$; $\chi_i$ is its mask and $\chi$ the total solid mask. $C_\eta$ controls the solid velocity penalty; $Re$ and $Pe$ are the Reynolds and Péclet numbers; and $\kappa$ is a coefficient in the paper's scalar-diffusion expression. $A_i$ is a matrix representing a spatial partial derivative in direction $i$; $Ap$ collects the pressure derivatives. $\partial_t$ is the partial derivative with respect to time. $\circ$ means element-by-element multiplication, $M$ is the grid-weighting matrix, and $H$ is conjugate transpose. A dagger marks an adjoint variable, used here as a Lagrange multiplier. $g_i(\mathbf x,t)$ is the prescribed geometry function, $\mathbf x$ is position, $t$ is time, and $T$ is final time. Indices $i,j,k$ identify coordinate components or stirrers according to context; repeated coordinate indices are summed.

**Groups of terms.**

- The first braces, multiplied by $\mathbf u^\dagger$, contain the momentum equation: time change, velocity advection, the solid-velocity penalty, pressure, and viscosity. $A_iA_i\mathbf u$ involves second spatial derivatives.
- The second braces, multiplied by $p^\dagger$, contain the pressure equation: second derivatives of pressure together with derivatives of the advection and penalty terms.
- The third braces, multiplied by $\theta^\dagger$, contain the scalar equation: time change, transport associated with fluid and solid velocities, and diffusion.
- The final bracket, multiplied by $\chi_i^\dagger$, is the geometry constraint: $\chi_i-g_i$ measures the difference between the mask and the prescribed geometry.

**Whole equation.** It combines the mixing score with the momentum, pressure, scalar, and geometry constraints so that their effects can be included in the sensitivity calculation.

**Printed inconsistencies.** The pressure term here omits a velocity factor present in equation 2.14, and the solid-advection term has a different sign from equation 2.13. The expression above follows the printed 3.4.

### Equation 3.5

$$
\begin{aligned}
\partial_t u_i^\dagger
&-\Pi_k^\dagger\circ[A_i u_k]
-A_j^H[u_j\circ\Pi_i^\dagger]
-\frac{\chi}{C_\eta}\circ\Pi_i^\dagger\\
&+Re^{-1}A_j^H A_j^H u_i^\dagger
-(1-\chi)\circ\theta^\dagger\circ[A_i\theta]=0.
\end{aligned}
$$

**Symbols.** $u_i^\dagger$ is an adjoint velocity component, a sensitivity variable rather than physical velocity. $u_j$ and $u_k$ are forward velocity components. $\Pi_i^\dagger$ and $\Pi_k^\dagger$ combine velocity and pressure adjoints, as defined after 3.9. $\theta$ and $\theta^\dagger$ are the scalar and its adjoint. $\chi$ is the solid mask, $C_\eta$ the penalty parameter, and $Re$ the Reynolds number. $A_i$ represents a spatial partial derivative; $A_j^H$ is the conjugate transpose of a derivative matrix. $\partial_t$ is the time derivative, $\circ$ is elementwise multiplication, and $i,j,k$ are coordinate indices.

**Groups of terms.** The first term changes the adjoint velocity in time. The next two contain forward velocity or its derivatives and represent sensitivity through fluid advection. The $\chi/C_\eta$ term represents the solid penalty, the $Re^{-1}$ term viscosity, and the last term connects velocity sensitivity to scalar gradients and the scalar adjoint.

**Whole equation.** It is the adjoint velocity equation, used to propagate information about how earlier flow changes affect the final score.

### Equation 3.6

$$
A_j^H\Pi_j^\dagger=0.
$$

**Symbols.** $A_j^H$ is the conjugate transpose of the spatial-derivative matrix in direction $j$; $\Pi_j^\dagger$ is component $j$ of the combined velocity–pressure adjoint quantity; and repeated $j$ means sum over coordinate directions.

**Group of terms.** The expression applies the transposed derivative matrices to the components of $\Pi^\dagger$ and sums them.

**Whole equation.** It is an adjoint constraint associated with the pressure treatment.

### Equation 3.7

$$
\begin{aligned}
\partial_t\theta^\dagger
&-A_j^H[(1-\chi)\circ u_j\circ\theta^\dagger]\\
&+A_i^H\left([Pe^{-1}(1-\chi)+\kappa\chi]\circ A_i^H\theta^\dagger\right)\\
&-A_j^H[\chi_i\circ(\mathbf u_{s,i})_j\circ\theta^\dagger]=0.
\end{aligned}
$$

**Symbols.** $\theta^\dagger$ is the scalar adjoint; $\chi$ and $\chi_i$ are the total and individual solid masks. $u_j$ is fluid-velocity component $j$, and $(\mathbf u_{s,i})_j$ is component $j$ of stirrer $i$'s velocity. $Pe$ and $\kappa$ are the paper's scalar-diffusion coefficients. $A_i^H$ and $A_j^H$ are conjugate-transposed spatial-derivative matrices, $\partial_t$ is the time derivative, and $\circ$ is elementwise multiplication. The indices identify stirrers or spatial directions according to context.

**Groups of terms.** The first term changes scalar sensitivity in time. The second represents transport by fluid velocity; the third represents scalar diffusion, with its coefficient depending on the mask; and the last represents transport associated with the solid velocity.

**Whole equation.** It propagates sensitivity to scalar changes backward through the modeled scalar transport.

### Equation 3.8

$$
\mathbf u^\dagger(\mathbf x,T)=0,
\qquad
\theta^\dagger(\mathbf x,T)=\frac{2}{V_\Omega}(A^{-2/3})^H M(A^{-2/3}\theta).
$$

**Symbols.** $\mathbf u^\dagger$ and $\theta^\dagger$ are velocity and scalar adjoints; $\mathbf x$ is position and $T$ final time. $V_\Omega$ is domain volume or area, $A^{-2/3}$ is the fractional operation in the score, $H$ denotes conjugate transpose, $M$ is the grid-weighting matrix, and $\theta$ is the final forward scalar field.

**Groups of terms.** The first condition sets the final velocity adjoint to zero. The second forms a final scalar-adjoint value from the final scalar field and the operator used in the score.

**Whole equation.** These are the final-time conditions for the backward adjoint calculation. The printed scalar condition resembles a derivative of a squared norm, whereas equation 3.2 prints a square root; the paper does not explain the difference in scaling.

### Equation 3.9

The paper prints the last term with an **unclosed parenthesis**. The parenthesis below is rendered as text so that the equation remains displayable in KaTeX without silently inventing a closing parenthesis.

$$
\chi_i^\dagger=\left[\theta^\dagger\circ[A_j\theta]-\frac{\Pi_j^\dagger}{C_\eta}\right]
\circ\left(u_j-(\mathbf u_{s,i})_j\right)
+\text{(}\kappa-Pe^{-1}A_j^H\theta^\dagger\circ A_j\theta.
$$

**Symbols.** $\chi_i^\dagger$ is the adjoint quantity associated with the mask of stirrer $i$. $\theta$ and $\theta^\dagger$ are the scalar and its adjoint. $A_j\theta$ is the discrete spatial derivative of the scalar in direction $j$; $A_j^H\theta^\dagger$ applies the conjugate-transposed derivative matrix to the scalar adjoint. $\Pi_j^\dagger$ is a combined velocity–pressure adjoint component, $C_\eta$ is the penalty parameter, $u_j$ and $(\mathbf u_{s,i})_j$ are fluid and solid velocity components, and $\kappa$ and $Pe$ are scalar-transport coefficients. $\circ$ denotes elementwise multiplication.

**Groups of terms.** The bracket combines scalar-gradient sensitivity with solid-penalty sensitivity and multiplies their combination by fluid velocity minus solid velocity. The last printed group contains diffusion coefficients and scalar and adjoint-scalar derivatives; its exact grouping is unclear because the closing parenthesis is missing.

**Whole equation.** It is the mask-related optimality expression used to connect the adjoint calculation to a geometry change.

Immediately afterward, the paper defines:

$$
\Pi_i^\dagger=u_i^\dagger+A_i^H p^\dagger.
$$

Here $u_i^\dagger$ is velocity-adjoint component $i$, $p^\dagger$ is the pressure adjoint, and $A_i^H$ is the conjugate-transposed derivative matrix. The two terms combine into $\Pi_i^\dagger$.

## Section 3.3: Complex shape parameterisation

### Equations 3.10a and 3.10b

$$
f_x(\alpha)=\frac{a_0}{2}+\sum_{k=1}^{n}[a_k\cos(k\alpha)-b_k\sin(k\alpha)],
$$

$$
f_y(\alpha)=\frac{c_0}{2}+\sum_{k=1}^{n}[c_k\cos(k\alpha)-d_k\sin(k\alpha)].
$$

**Symbols.** $f_x,f_y$ are coordinates of a boundary point. $\alpha$ travels around the outline from $0$ to $2\pi$; it is not time. $a_0,c_0$ are constant coordinate terms; $a_k,b_k,c_k,d_k$ are adjustable shape coefficients; $k$ is the Fourier-mode index; and $n$ is the number of retained modes, not the grid size from 3.3.

**Groups of terms.** Each constant term shifts its coordinate. Each sine–cosine pair specifies a pattern of coordinate variation around the boundary. The sums combine those patterns.

**Whole equations.** They describe the stirrer boundary with finitely many coefficients. A change in one coefficient generally moves many points on the outline by different amounts.

### Equations 3.11a and 3.11b

$$
x=f_x(\alpha),
$$

$$
y=f_y(\alpha).
$$

**Symbols.** $x,y$ are Cartesian coordinates of a boundary point; $f_x,f_y$ are the functions in 3.10; and $\alpha$ is the boundary parameter.

**Groups of terms.** The two equations provide the horizontal and vertical coordinates for the same value of $\alpha$.

**Whole equations.** Together they define the boundary as a parametric curve.

### Equation 3.12

$$
f(a_i,b_i,c_i,d_i)=[f_x,f_y].
$$

**Symbols.** $f$ is the shape representation; $a_i,b_i,c_i,d_i$ are the shape coefficients; $f_x,f_y$ are the coordinate functions; and $i$ is the index used in the paper's compact notation.

**Group of terms.** The bracket combines the horizontal and vertical coordinate functions.

**Whole equation.** It states compactly that the outline depends on the Fourier coefficients.

### Equation 3.13

$$
w(\mathbf x_k)=\sum_{i=1}^{n}\phi_{i,i-1}.
$$

**Symbols.** $\mathbf x_k$ is the point being tested; $w(\mathbf x_k)$ is its total winding angle; $\phi_{i,i-1}$ is the signed angle between successive boundary points as viewed from $\mathbf x_k$; $i$ indexes sampled points along the outline; and $n$ is the number of sampled contributions in this discrete expression.

**Group of terms.** The sum adds the signed angular changes while travelling around the outline.

**Whole equation.** It tests whether the outline surrounds the point: for the orientation used by the paper, the total is $2\pi$ inside and zero outside.

### Equation 3.14

$$
\chi_i(\mathbf x,t)=\begin{cases}
1,&w_i(\mathbf x)=2\pi,\\
0,&w(\mathbf x)=0.
\end{cases}
$$

**Symbols.** $\chi_i$ is the mask for stirrer $i$; $\mathbf x,t$ are position and time; and $w_i,w$ are the paper's winding-angle notation for the inside/outside test.

**Groups of terms.** The first line assigns solid value 1 inside the outline; the second assigns fluid value 0 outside.

**Whole equation.** It converts the boundary curve into a sharp solid mask on the grid.

### Equation 3.15

$$
d=\min_\alpha\sqrt{(x-f_x)^2+(y-f_y)^2}.
$$

**Symbols.** $x,y$ are coordinates of the tested point, $f_x,f_y$ are coordinates of a boundary point, $\alpha$ is the boundary parameter, and $d$ is the shortest distance from the tested point to the boundary.

**Groups of terms.** The square root gives the distance to one boundary point; the minimum over $\alpha$ selects the closest one.

**Whole equation.** It calculates the distance needed to smooth the mask near the outline.

### Equation 3.16

$$
\chi_i(\mathbf x,t)=\begin{cases}
1,&w=2\pi\text{ and }d>h,\\
\dfrac12\left[1+\cos\left(\dfrac{\pi(h-d)}{h}\right)\right],&w=2\pi\text{ and }d<h,\\
0,&w=0.
\end{cases}
$$

**Symbols.** $\chi_i$ is the smoothed mask; $\mathbf x,t$ are position and time; $w$ is the winding angle indicating inside or outside; $d$ is distance to the boundary; $h$ is the smoothing-layer thickness; and $\pi$ is the circle constant.

**Groups of terms.** The first line gives mask value 1 well inside the rod, the cosine expression gives values between 0 and 1 in the inner boundary layer, and the last line gives 0 outside.

**Whole equation.** It replaces the sharp mask edge with a smooth transition as the boundary moves across the grid.

### Equation 3.17

$$
\frac{\partial\mathcal L}{\partial a_k}=\frac{\partial\mathcal L}{\partial\chi_i}\frac{\partial\chi_i}{\partial d}\frac{\partial d}{\partial a_k}.
$$

**Symbols.** $\mathcal L$ is the augmented cost; $a_k$ is a shape coefficient; $\chi_i$ is the mask of stirrer $i$; and $d$ is distance from a grid point to the boundary. A partial derivative describes the local rate of change with respect to the variable underneath it.

**Groups of terms.** $\partial d/\partial a_k$ describes coefficient change to distance change; $\partial\chi_i/\partial d$ describes distance change to mask change; and $\partial\mathcal L/\partial\chi_i$ describes sensitivity of the augmented cost to the mask.

**Whole equation.** It applies the chain rule to connect a shape coefficient to the cost through the distance and mask. A full coefficient sensitivity combines contributions over positions and times.

### Equation 3.18

$$
\left.\frac{\partial d}{\partial a_k}=\frac{(f_x-x)\cos(k\alpha)}{d}\right|_{\tilde\alpha}.
$$

**Symbols.** $d$ is shortest distance to the outline; $a_k$ is the shape coefficient; $f_x$ is a boundary point's horizontal coordinate; $x$ is the tested grid point's horizontal coordinate; $\alpha$ is the boundary parameter; $\tilde\alpha$ is its value at the closest boundary point; and $k$ is the mode index.

**Groups of terms.** $\cos(k\alpha)$ describes how changing $a_k$ moves the boundary's horizontal coordinate; $(f_x-x)/d$ relates that displacement to the direction from the grid point to the boundary. The subscript $\tilde\alpha$ says to evaluate at the closest point.

**Whole equation.** It gives the local change in closest distance caused by a small change in $a_k$, under suitable smoothness and uniqueness conditions.

## Area equations in section 3.3

### Equation 3.19

$$
A=-\int_{\alpha=0}^{\alpha=2\pi}f_y\,df_x.
$$

**Symbols.** $A$ is the oriented area enclosed by the outline; $f_x,f_y$ are boundary coordinates; $df_x$ is a small change in horizontal coordinate; and $\alpha=0$ to $2\pi$ is one traversal of the outline.

**Group of terms.** The integral combines vertical coordinate $f_y$ with horizontal changes $df_x$ around the curve.

**Whole equation.** It calculates the oriented enclosed area from the boundary.

### Equation 3.20

$$
A=-\int_0^{2\pi}f_y\frac{\partial f_x}{\partial\alpha}\,d\alpha.
$$

**Symbols.** $A$ is area; $f_x,f_y$ are boundary coordinates; $\alpha$ is the boundary parameter; $\partial f_x/\partial\alpha$ is the rate of change of the horizontal coordinate with the parameter; and $d\alpha$ is a small parameter interval.

**Group of terms.** The derivative and $d\alpha$ express horizontal change along the curve.

**Whole equation.** It writes the area calculation in terms of $\alpha$.

### Equation 3.21

$$
\begin{aligned}
A=-\int_0^{2\pi}&\left[\frac{c_0}{2}+\sum_{k=1}^{n}(c_k\cos(k\alpha)-d_k\sin(k\alpha))\right]\\
&\left[\sum_{l=1}^{n}l(-a_l\sin(l\alpha)-b_l\cos(l\alpha))\right]d\alpha.
\end{aligned}
$$

**Symbols.** $A$ is oriented area; $a_l,b_l,c_k,d_k,c_0$ are Fourier coefficients; $k,l$ are mode indices; $n$ is the number of retained modes; and $\alpha,d\alpha$ are the boundary parameter and a small parameter interval.

**Groups of terms.** The first bracket is $f_y$; the second is the derivative of $f_x$ with respect to $\alpha$. The integral combines their product around the outline.

**Whole equation.** It substitutes the Fourier parameterization into the area integral.

### Equation 3.22

$$
A=\sum_{k=0}^{n}\sum_{l=1}^{n}l\left(\int_0^{2\pi}[c_k\cos(k\alpha)-d_k\sin(k\alpha)][a_l\sin(l\alpha)+b_l\cos(l\alpha)]\,d\alpha\right).
$$

**Symbols.** $A$ is area; $a_l,b_l,c_k,d_k$ are Fourier coefficients; $k,l$ are mode indices; $n$ is the number of modes; and $\alpha,d\alpha$ are the boundary parameter and interval.

**Groups of terms.** The first bracket contains vertical-coordinate modes, the second contains differentiated horizontal-coordinate modes, and the double sum considers combinations of modes $k$ and $l$.

**Whole equation.** It rearranges the area integral so that the Fourier products can be evaluated. The paper says it has absorbed the factor $1/2$ into its notation for $c_0$.

### Equation 3.23

$$
\begin{aligned}
A=\sum_{k=0}^{n}\sum_{l=1}^{n}l\Bigg(\int_0^{2\pi}
&c_kb_l\cos(k\alpha)\cos(l\alpha)+c_ka_l\cos(k\alpha)\sin(l\alpha)\\
&-d_ka_l\sin(k\alpha)\sin(l\alpha)-d_kb_l\sin(k\alpha)\cos(l\alpha)\,d\alpha\Bigg).
\end{aligned}
$$

**Symbols.** $A$ is area; $a_l,b_l,c_k,d_k$ are shape coefficients; $k,l$ are mode indices; $n$ is the number of modes; and $\alpha,d\alpha$ are the boundary parameter and integration interval.

**Groups of terms.** The four terms are cosine–cosine, cosine–sine, sine–sine, and sine–cosine products. The factor $l$ comes from differentiating the horizontal-coordinate modes.

**Whole equation.** It expands 3.22 so each trigonometric product can be integrated.

### Equation 3.24

$$
\sum_{k=0}^{n}\sum_{l=1}^{n}\int_0^{2\pi}c_kb_l\cos(k\alpha)\cos(l\alpha)\,d\alpha
=\sum_{k=0}^{n}\pi c_kb_k.
$$

**Symbols.** $c_k,b_l,b_k$ are Fourier coefficients; $k,l$ are mode indices; $n$ is the number of modes; and $\alpha$ is the boundary parameter.

**Group of terms.** The left combines cosine modes; the right retains matching-mode contributions.

**Whole equation.** It states the cosine–cosine contribution. The printed right-hand index includes $k=0$, although the earlier series starts the nonconstant $b_k$ coefficients at $k=1$.

### Equation 3.25

$$
\sum_{k=0}^{n}\sum_{l=1}^{n}\int_0^{2\pi}c_ka_l\cos(k\alpha)\sin(l\alpha)\,d\alpha=0.
$$

**Symbols.** $c_k,a_l$ are Fourier coefficients; $k,l$ are mode indices; $n$ is the number of modes; and $\alpha$ is the boundary parameter.

**Group of terms.** Each product combines a cosine mode with a sine mode over a full period.

**Whole equation.** The cosine–sine cross-products integrate to zero.

### Equation 3.26

$$
\sum_{k=1}^{n}\sum_{l=1}^{n}\int_0^{2\pi}d_kb_l\sin(k\alpha)\cos(l\alpha)\,d\alpha=0.
$$

**Symbols.** $d_k,b_l$ are Fourier coefficients; $k,l$ are mode indices; $n$ is the number of modes; and $\alpha$ is the boundary parameter.

**Group of terms.** Each product combines a sine mode with a cosine mode over a full period.

**Whole equation.** The sine–cosine cross-products also integrate to zero.

### Equation 3.27

$$
\sum_{k=1}^{n}\sum_{l=1}^{n}\int_0^{2\pi}d_ka_l\sin(k\alpha)\sin(l\alpha)\,d\alpha
=\sum_{k=1}^{n}\pi d_ka_k.
$$

**Symbols.** $d_k,a_l,a_k$ are Fourier coefficients; $k,l$ are mode indices; $n$ is the number of modes; and $\alpha$ is the boundary parameter.

**Group of terms.** The left combines sine modes; the right retains matching-mode contributions.

**Whole equation.** It gives the sine–sine contribution.

In 3.24–3.27, the factor $l$ shown outside the integrals in 3.23 is omitted from the intermediate printed lines; the mode factor appears again in the final area formula.

### Equation 3.28

$$
A=\sum_{k=1}^{n}\pi k(c_kb_k-d_ka_k).
$$

**Symbols.** $A$ is the oriented area; $a_k,b_k,c_k,d_k$ are mode-$k$ Fourier coefficients; $k$ is the mode index; and $n$ is the number of modes.

**Groups of terms.** $c_kb_k$ and $d_ka_k$ combine horizontal and vertical coefficients of the same mode; $\pi k$ weights that mode; and the sum combines all modes.

**Whole equation.** It calculates oriented area directly from the shape coefficients.

### Equation 3.29

$$
\widetilde A=\sum_{k=1}^{n}\pi k(\widetilde c_k\widetilde b_k-\widetilde d_k\widetilde a_k).
$$

**Symbols.** $\widetilde A$ is the initial target area; $\widetilde a_k,\widetilde b_k,\widetilde c_k,\widetilde d_k$ are initial shape coefficients; $k$ is the mode index; and $n$ is the number of modes.

**Group of terms.** This applies the area formula from 3.28 to the initial coefficients.

**Whole equation.** It defines the area that later shape updates should preserve.

### Equation 3.30

$$
\begin{aligned}
\sum_{k=1}^{n}\pi k\left(
\sqrt{\frac{\widetilde A}{A}}\,c_k\sqrt{\frac{\widetilde A}{A}}\,b_k
-\sqrt{\frac{\widetilde A}{A}}\,d_k\sqrt{\frac{\widetilde A}{A}}\,a_k\right)
=\frac{\widetilde A}{A}\sum_{k=1}^{n}\pi k(c_kb_k-d_ka_k).
\end{aligned}
$$

**Symbols.** $A$ is the proposed shape's area, $\widetilde A$ is the initial target area, $a_k,b_k,c_k,d_k$ are proposed coefficients, $k$ is the mode index, and $n$ is the number of modes. The square-root factor is applied to each relevant shape coefficient.

**Groups of terms.** On the left, each coefficient is scaled; each area term contains two scaled coefficients. On the right, the two square-root factors have combined into $\widetilde A/A$.

**Whole equation.** It shows how uniform coefficient scaling changes the calculated area.

### Equation 3.31

$$
=\frac{\widetilde A}{A}A.
$$

**Symbols.** $A$ is the candidate area before normalization and $\widetilde A$ is the target area.

**Group of terms.** The ratio $\widetilde A/A$ multiplies the candidate area.

**Whole equation.** It follows from 3.30 after substituting the unscaled area formula from 3.28.

### Equation 3.32

$$
=\widetilde A.
$$

**Symbols.** $\widetilde A$ is the original target area.

**Group of terms.** The candidate area $A$ in 3.31 cancels with the denominator.

**Whole equation.** The normalized shape has the target area. The normalization rescales the shape after an update, so it can alter both coordinate functions even if the initial update affected only one coefficient.
