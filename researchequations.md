# Time to stir: equations

Sources: [MSJ] Murthy Shekhar & Jayanti (2002), the paper on unbaffled vessels · [H] Halász et al. (2007), the magnetic-stirrer paper · your notes, with the date of the entry · standard: a textbook result · my choice: an assumption made in the chat.

## 1 · A: original equations, taken as given

**A1 · Tracer transport**

$\dfrac{\partial(\rho\phi)}{\partial t} + \nabla\cdot\left(\rho\,\mathbf{u}\,\phi - \Gamma_\phi\nabla\phi\right) = S_\phi, \qquad \Gamma_\phi = \rho\,(D + D_t)$

Source: [MSJ] Eq. (5), p. 484; your notes (2 and 8 Oct). Meaning: the dye in a small fixed region changes because the flow carries dye in and out and because dye diffuses down its concentration gradient. $S_\phi$ would be dye made by a reaction; here it is 0. $\phi$ is the dye concentration, written $c$ from B1 on; $D$ and $D_t$ are the molecular and turbulent diffusivities.

**A2 · Continuity**

$\nabla\cdot\mathbf{u} = 0$

Source: [MSJ] Eq. (1), p. 483; your notes (2 Oct). Meaning: the liquid is incompressible, so as much flows out of any small region as flows in.

**A3 · Burgers vortex**

$v_r = -\dfrac{2\nu}{c^2}\,r, \qquad v_t = \dfrac{C}{r}\left(1 - e^{-r^2/c^2}\right), \qquad v_z = \dfrac{4\nu}{c^2}\,z$

Source: [H] Eq. (2); your notes (22 Sept). Meaning: a steady vortex in which inflow towards the axis ($v_r$) and vertical stretching ($v_z$) balance viscous spreading. Inside the core radius $c$ the liquid turns like a solid body; outside it the swirl $v_t$ falls off as $C/r$. $C$ sets the strength, $\nu$ is the kinematic viscosity, and $z$ is measured from the level with no vertical flow. $v_t$ is the $u_\theta$ of your equation.

**A4 · Halász's fits to measurements in water**

$\Delta h = \dfrac{\Omega^2 a^2 d^2 R^{1/2}}{\nu\,(\alpha H + kR)\,g^{1/2}}, \qquad c \approx b = \dfrac{\beta a \nu}{d\sqrt{gR}}, \qquad \alpha = 580,\ \ k = 2800,\ \ \beta = 2800$

Source: [H] Eqs. (12), (16), (22); your notes (22 Sept). Meaning: the measured funnel depth $\Delta h$ grows with the square of the stirring speed $\Omega$ and with the bar's size; the core radius $c$, equal to the funnel's half-width $b$, does not depend on speed. $a$ is the bar's half-length, $d$ its width, $R$ the beaker radius, $H$ the liquid depth at rest and $g$ gravity. Measured in water at $\Omega = 20$–$120$ rad/s, with $R \gt 0.4H$.

**A5 · Funnel depth of a Burgers vortex**

$\Delta h = \ln 2\,\dfrac{C^2}{c^2 g}$

Source: [H] Eq. (20); your notes (22 Sept). Meaning: the depth of the dip that a Burgers vortex of strength $C$ and core radius $c$ makes in the free surface.

**A6 · Free surface, with the volume fixed**

$\dfrac{d\eta}{dr} = \dfrac{v_t^2}{r\,g}, \qquad \displaystyle\int_0^R 2\pi r\,\eta\,dr = \pi R^2 H$

Source: [H] Eq. (18); your notes (2 Oct). Meaning: the surface height $\eta(r)$ slopes so that gravity balances the centripetal acceleration of the swirling liquid; spinning does not change the amount of liquid, so the volume under the surface stays $\pi R^2 H$.

**A7 · Eddy diffusivity**

$D_t = \dfrac{\nu_t}{\mathrm{Sc}_t}, \qquad \mathrm{Sc}_t = 0.7$

Source: your notes (2 Oct), a standard turbulence-model relation; the value 0.7 is my choice. Meaning: turbulent eddies spread dye at about the rate they spread momentum (the eddy viscosity $\nu_t$); the turbulent Schmidt number $\mathrm{Sc}_t$ is the ratio of the two.

**A8 · Molecular diffusivity**

$D = 10^{-9}\ \mathrm{m^2/s}$

Source: standard value for a dye in water; [MSJ] gives none. Meaning: how fast dye spreads by molecular motion alone, with no flow.

**A9 · Mixing criterion**

$\left|\dfrac{c}{c_\infty} - 1\right| \le 0.05 \ \text{ everywhere}, \qquad t_{95} = \text{the first time this holds}$

Source: [MSJ] pp. 484, 497. Meaning: mixed means every point is within 5 % of the final, uniform concentration $c_\infty$.

**A10 · Hybrid scheme for one cell face**

$F = Q\,\dfrac{c_\mathrm{P} + c_\mathrm{N}}{2} - G\,(c_\mathrm{N} - c_\mathrm{P}) \ \text{ if } |Q| \le 2G, \qquad F = Q\,c_\mathrm{P} \ \text{ if } Q \gt 2G, \qquad F = Q\,c_\mathrm{N} \ \text{ if } Q \lt -2G$

The same, written compactly: $F = b_\mathrm{PN}\,c_\mathrm{P} - b_\mathrm{NP}\,c_\mathrm{N}, \qquad b_\mathrm{PN} = \max(Q,\ G + Q/2,\ 0), \qquad b_\mathrm{NP} = \max(-Q,\ G - Q/2,\ 0)$

Source: [MSJ] p. 486 (the scheme CFX uses). Meaning: $F$ is the dye flowing per second from cell P into its neighbour N, $Q$ the liquid flowing through the face (B8) and $G$ its diffusion conductance (B9). The dye on the face is the average of the two cells, unless flow beats diffusion ($|Q|/G \gt 2$, a mesh Péclet number above 2); then the upstream cell's value is used and diffusion through that face is dropped.

**A11 · BDF2 time stepping, for $dy/dt = f(y)$**

$\dfrac{3y^{n+1} - 4y^{n} + y^{n-1}}{2\,\Delta t} = f\!\left(y^{n+1}\right), \qquad \text{first step: } \dfrac{y^{1} - y^{0}}{\Delta t} = f\!\left(y^{1}\right)$

Source: standard numerical method (second-order backward differentiation formula); the first step is backward Euler, because BDF2 needs two earlier values. Meaning: a stable, second-order way of stepping ordinary differential equations forward in time.

**A12 · Starting dye ring**

$c(r, z, 0) \propto \exp\!\left[-\dfrac{(r - R/2)^2 + (z - H + 3\ \mathrm{mm})^2}{2w^2}\right], \qquad w = 3\ \mathrm{mm}, \ \text{scaled so } c_\infty = 1$

Source: my choice. Meaning: the dye starts as a thin ring halfway to the wall, 3 mm under the surface; the scaling makes the fully mixed concentration 1.

**A13 · Ring-shaped grid cell**

$\text{side face: } 2\pi r\,\Delta z, \qquad \text{top and bottom faces: } \pi\left(r_+^2 - r_-^2\right), \qquad \text{volume: } V = \pi\left(r_+^2 - r_-^2\right)\Delta z$

Source: standard geometry. Meaning: the face areas and volume of a cell between radii $r_-$ and $r_+$ and height $\Delta z$; the factors of $r$ in your equation end up here.

**A14 · Stirring speed**

$\Omega = \dfrac{2\pi \times \mathrm{rpm}}{60}\ \mathrm{rad/s}$

Source: standard unit conversion. Meaning: turns revolutions per minute into angular speed in radians per second; Halász's formulas use $\Omega$, not revolutions per second.

**A15 · No dye crosses any boundary**

$(D + D_t)\,\dfrac{\partial c}{\partial n} = 0 \ \text{ on the wall, bottom, surface and axis}$

Source: [MSJ] p. 484 (Neumann conditions). Meaning: no dye diffuses through any boundary ($n$ is the direction normal to it). No liquid crosses them either, because $\psi = 0$ there (B4).

**A16 · Time step**

$\Delta t = 0.5 \times \dfrac{\text{cell size}}{\text{fastest } r\text{--}z \text{ velocity}}$

Source: my choice. Meaning: in one step the liquid moves at most half a cell (the cells are 1.25 mm).

## 2 · B: derived equations, each from the A equations named

**B1 · Your equation, the one being solved**

$\dfrac{\partial c}{\partial t} + u_r\dfrac{\partial c}{\partial r} + u_z\dfrac{\partial c}{\partial z} = \dfrac{1}{r}\dfrac{\partial}{\partial r}\left[r\,(D + D_t)\dfrac{\partial c}{\partial r}\right] + \dfrac{\partial}{\partial z}\left[(D + D_t)\dfrac{\partial c}{\partial z}\right]$

From: A1 with $\phi = c$, constant $\rho$ and no source, divided by $\rho$; A2 turns $\nabla\cdot(\mathbf{u}c)$ into $\mathbf{u}\cdot\nabla c$; $\nabla$ written out in $r$, $\theta$, $z$; then nothing varies with $\theta$ (axisymmetry, your assumption). Also in your notes (2 Oct).

**B2 · Swirl strength**

$C = A\,\Omega, \qquad A = a^2\left[\dfrac{\beta^2\nu}{\ln 2\,(\alpha H + kR)\sqrt{gR}}\right]^{1/2}$

From: solve A5 for $C$, knowing $\Delta h$ and $c$ from A4 (the two funnel depths set equal). This is [H] Eq. (21); your notes (22 Sept).

**B3 · Peak swirl**

$v_{t,\max} = 0.638\,\dfrac{C}{c} \quad \text{at } r = 1.12\,c$

From: set $dv_t/dr = 0$ in A3's $v_t$ and solve numerically.

**B4 · Closed loop in the $r$–$z$ plane (an assumption, not derived)**

$\psi = -\dfrac{U_s}{2}\,r^2\left(1 - \dfrac{r^2}{R^2}\right)\sin\dfrac{\pi z}{H}$

$u_r = -\dfrac{1}{r}\dfrac{\partial\psi}{\partial z} = \dfrac{\pi U_s}{2H}\,r\left(1 - \dfrac{r^2}{R^2}\right)\cos\dfrac{\pi z}{H}$

$u_z = \dfrac{1}{r}\dfrac{\partial\psi}{\partial r} = -U_s\left(1 - \dfrac{2r^2}{R^2}\right)\sin\dfrac{\pi z}{H}$

$U_s = \kappa_s\,v_{t,\max}, \qquad \kappa_s = 0.1$

From: my choice, not derived. $\psi = 0$ on every boundary, so no liquid crosses the wall, bottom, surface or axis, and A2 holds automatically. The shape follows [H] Fig. 8 (one loop: out along the bottom, up the wall, in at the surface, down the axis); $U_s$ growing in proportion to $\Omega$ follows [H]; $\kappa_s = 0.1$ follows [MSJ] p. 487 (radial velocities about an order of magnitude below the swirl); $v_{t,\max}$ is B3. $U_s$ is the peak downflow, on the axis at mid-depth.

**B5 · Flow near the surface centre**

$u_r \approx -\dfrac{\alpha_s}{2}\,r, \qquad u_z \approx -\alpha_s\,(H - z), \qquad \alpha_s = \dfrac{\pi U_s}{H}$

From: B4's $u_r$ and $u_z$ for small $r$ and $z$ near the surface $H$. They have the same form as A3's $v_r$ and $v_z$, with $\alpha_s$ in place of $4\nu/c^2$.

**B6 · Core balance, giving the eddy viscosity**

$\nu + \nu_t = \dfrac{\alpha_s\,c^2}{4}$

From: A3's $v_r$ equals B5's $u_r$ when $4\nu/c^2 = \alpha_s$. Turbulence is assumed to act as extra viscosity, so $\nu$ becomes $\nu + \nu_t$ (my assumption). Solved for $\nu_t$, knowing $c$ from A4 and $\alpha_s$ from B5; $D_t$ then follows from A7.

**B7 · Height of the funnel tip**

$\eta(r) - h = \displaystyle\int_0^r \dfrac{v_t(r')^2}{g\,r'}\,dr', \qquad h = H - \dfrac{2}{R^2}\displaystyle\int_0^R r\,\big[\eta(r) - h\big]\,dr, \qquad \text{fastest usable speed: } h = d$

From: solve A6's $d\eta/dr$ outward from the tip ($r = 0$, height $h$), knowing $v_t$ from A3; then put $\eta = h + (\eta - h)$ into A6's volume condition and solve for $h$. $h = d$ is my assumption: the tip reaches the top of the bar, taking the bar's height equal to its width $d$.

**B8 · Liquid flow through each cell face**

Side face at $r_f$, from $z_-$ to $z_+$: $Q = -2\pi\left[\psi(r_f, z_+) - \psi(r_f, z_-)\right]$

Top or bottom face at $z_f$, from $r_-$ to $r_+$: $Q = 2\pi\left[\psi(r_+, z_f) - \psi(r_-, z_f)\right]$

From: integrate B4's $u_r$ over the side face (area element $2\pi r_f\,dz$) and $u_z$ over the top or bottom face (area element $2\pi r\,dr$). Built this way, A2 holds exactly on the grid.

**B9 · Diffusion conductance of each face**

$\text{side: } G = (D + D_t)\,\dfrac{2\pi r_f\,\Delta z}{\Delta r}, \qquad \text{top or bottom: } G = (D + D_t)\,\dfrac{\pi\left(r_+^2 - r_-^2\right)}{\Delta z}$

From: B1's diffusive flux, $(D + D_t)\,\partial c/\partial n$, across one face, with the face area from A13 and the gradient approximated as $(c_\mathrm{N} - c_\mathrm{P})$ divided by the distance between the two cell centres. $D$ from A8, $D_t$ from A7 and B6.

**B10 · Dye balance on each cell**

$V_\mathrm{P}\,\dfrac{dc_\mathrm{P}}{dt} = \sum_\mathrm{N}\left(b_\mathrm{NP}\,c_\mathrm{N} - b_\mathrm{PN}\,c_\mathrm{P}\right), \qquad \text{all 3,864 cells at once: } \mathbf{V}\,\dfrac{d\mathbf{c}}{dt} = \mathbf{K}\,\mathbf{c}$

From: integrate B1 over one ring cell (B1 written back in conservation form using A2; the divergence theorem then turns it into flows through the four faces). The flows come from A10, with $Q$ from B8 and $G$ from B9; the cell volume $V_\mathrm{P}$ from A13; boundary faces carry nothing (A15). $\mathbf{K}$ holds the $b$ coefficients; $\mathbf{V}$ is the diagonal matrix of cell volumes.

**B11 · One time step**

$\left(3\mathbf{V} - 2\,\Delta t\,\mathbf{K}\right)\mathbf{c}^{n+1} = \mathbf{V}\left(4\mathbf{c}^{n} - \mathbf{c}^{n-1}\right), \qquad \text{first step: } \left(\mathbf{V} - \Delta t\,\mathbf{K}\right)\mathbf{c}^{1} = \mathbf{V}\,\mathbf{c}^{0}$

From: apply A11 to B10 and multiply through by $2\,\Delta t\,\mathbf{V}$ (first step: by $\Delta t\,\mathbf{V}$). $\Delta t$ from A16; $\mathbf{c}^0$ from A12.

## 3 · What is typed into the code

**Numbers typed in**

- $g = 9.81\ \mathrm{m/s^2}$, $\nu = 1.0\times10^{-6}\ \mathrm{m^2/s}$ (water), $D = 1.0\times10^{-9}\ \mathrm{m^2/s}$ (A8)
- Beaker: $R = 5.25$ cm, $H = 11.5$ cm (1 L of water)
- Bars $(a, d)$: (2.05, 0.85), (2.50, 0.90) and (4.00, 1.00) cm, from [H] Table 2
- Halász's constants: $\alpha = 580$, $k = 2800$, $\beta = 2800$ (A4)
- Assumptions: $\kappa_s = 0.1$ (B4), $\mathrm{Sc}_t = 0.7$ (A7)
- Speeds: 200, 300, …, 1200 rpm
- Numerics: 42 × 92 cells of 1.25 mm, time-step factor 0.5 (A16), tolerance 0.05 (A9), dye ring at $R/2$, 3 mm deep, $w = 3$ mm (A12)

**Formulas, in the order the script runs them**

**1 · A14 · `omega`**

$\Omega = \dfrac{2\pi \times \mathrm{rpm}}{60}$

**2 · A4 · `c`**

$c = \dfrac{\beta a \nu}{d\sqrt{gR}}$

**3 · B2 · `A`, `C`**

$A = a^2\left[\dfrac{\beta^2\nu}{\ln 2\,(\alpha H + kR)\sqrt{gR}}\right]^{1/2}, \qquad C = A\,\Omega$

**4 · A5 · `dh`**

$\Delta h = \ln 2\,\dfrac{C^2}{c^2 g}$

Printed in the results table only; not used in the simulation.

**5 · A3, $v_t$ only · `vt`**

$v_t = \dfrac{C}{r}\left(1 - e^{-r^2/c^2}\right)$

On a fine grid of $r$ from 0 to $R$.

**6 · A6, first part · `rise`**

$\eta(r) - h = \displaystyle\int_0^r \dfrac{v_t(r')^2}{g\,r'}\,dr'$

Integrated by the trapezoid rule.

**7 · B7 · `h`, then `brentq`**

$h = H - \dfrac{2}{R^2}\displaystyle\int_0^R r\,\big[\eta(r) - h\big]\,dr, \qquad \text{solve } h = d \text{ for } \Omega$

Brent's root-finder finds the speed at which $h = d$. Faster speeds are dropped, and that top speed is added as the last point.

**8 · B3 · `vt_max`**

$v_{t,\max} = 0.638\,\dfrac{C}{c}$

**9 · B4 · `Us`**

$U_s = \kappa_s\,v_{t,\max}$

**10 · B5 · `alpha_s`**

$\alpha_s = \dfrac{\pi U_s}{H}$

**11 · B6 · `nu_t`**

$\nu_t = \max\!\left(\dfrac{\alpha_s\,c^2}{4} - \nu,\ 0\right)$

The max(…, 0) only stops a negative value; it never triggers here ($\nu_t/\nu$ is 9 to 145).

**12 · A7 · `Dt`**

$D_t = \dfrac{\nu_t}{\mathrm{Sc}_t}$

**13 · B4 · `psi`, at every cell corner**

$\psi = -\dfrac{U_s}{2}\,r^2\left(1 - \dfrac{r^2}{R^2}\right)\sin\dfrac{\pi z}{H}$

**14 · B8 · `Qr`, `Qz`, for every face**

$Q_\text{side} = -2\pi\left[\psi(r_f, z_+) - \psi(r_f, z_-)\right], \qquad Q_\text{top/bottom} = 2\pi\left[\psi(r_+, z_f) - \psi(r_-, z_f)\right]$

**15 · B9 · `Gr`, `Gz`, for every face**

$G_\text{side} = (D + D_t)\,\dfrac{2\pi r_f\,\Delta z}{\Delta r}, \qquad G_\text{top/bottom} = (D + D_t)\,\dfrac{\pi\left(r_+^2 - r_-^2\right)}{\Delta z}$

**16 · A10 · `b_pn`, `b_np`, for every face**

$b_\mathrm{PN} = \max(Q,\ G + Q/2,\ 0), \qquad b_\mathrm{NP} = \max(-Q,\ G - Q/2,\ 0)$

**17 · B10 with A13 and A15 · `V`, `K`**

$V_\mathrm{P} = \pi\left(r_+^2 - r_-^2\right)\Delta z, \qquad V_\mathrm{P}\,\dfrac{dc_\mathrm{P}}{dt} = \sum_\mathrm{N}\left(b_\mathrm{NP}\,c_\mathrm{N} - b_\mathrm{PN}\,c_\mathrm{P}\right)$

The $b$ coefficients are summed into the matrix $\mathbf{K}$; faces on the boundary are left out, so nothing crosses them.

**18 · A12 · `c`, here the dye concentration**

$c^0 \propto \exp\!\left[-\dfrac{(r - R/2)^2 + (z - H + 3\ \mathrm{mm})^2}{2w^2}\right]$

Scaled so its volume-weighted mean is 1. Same letter as the core radius in item 2, but a different variable in a different function.

**19 · A16 · `dt`**

$\Delta t = 0.5 \times \dfrac{1.25\ \mathrm{mm}}{\text{fastest } r\text{--}z \text{ velocity}}$

**20 · B11 · `step1`, `step2`**

$\left(\mathbf{V} - \Delta t\,\mathbf{K}\right)\mathbf{c}^{1} = \mathbf{V}\,\mathbf{c}^{0}, \qquad \text{then } \left(3\mathbf{V} - 2\,\Delta t\,\mathbf{K}\right)\mathbf{c}^{n+1} = \mathbf{V}\left(4\mathbf{c}^{n} - \mathbf{c}^{n-1}\right)$

Both matrices are LU-factorised once and reused at every step.

**21 · A9 · `dev`, `t_mix`**

$\text{after every step: } \max_\text{cells}|c - 1| \le 0.05\ ?$

The first time it is, interpolated between the two steps either side, is $t_{95}$.

**Not typed in**

- A1, A2 and B1: they enter only through B10. A2 is also built into B4 and B8.
- A3's $v_r$ and $v_z$: used only to derive B5 and B6; B4 replaces them.
- A4's $\Delta h$: used only through B2.
- Computed for output only: $\sigma$ (the volume-weighted RMS deviation), the exponential-tail fit, the table, the CSV and the plots.