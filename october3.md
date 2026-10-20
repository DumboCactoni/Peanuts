# evan chen

##### 4
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [ ] 41
- [ ] 45
- [ ] 46
- [ ] 48
- [ ] 51
- [ ] 52

##### 5 reading
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [x] 5
- [x] 6
- [x] 7
- [x] 8
- [x] 9
- [x] 10
- [x] 11
- [x] 12
#####  5problems
- [ ] 13
- [ ] 14
- [ ] 15
- [ ] 16
- [ ] 17
- [ ] 18
- [ ] 19
- [ ] 20
- [ ] 21
- [ ] 22
- [ ] 23
- [ ] 24
- [ ] 25
- [ ] 26
- [ ] 27
- [ ] 28
- [ ] 29
- [ ] 30
# codeforces, papers
- [x] color the fence
- [x] graph without long paths
- [x] zero path
- [x] baby ehab partitions
- [x] preflix flip hard
- [x] array destruction
- [x] and or and square sum
- [x] cover it

do till 22
### 2020amc12a
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [x] 5
- [ ] almost
### 2020amc12b >20
- [x] 1
- [x] 2
- [x] 3
- [ ] 4
- [ ] 5
### 2021amc12a >10feq
- [x] 1
- [x] 2
- [x] 3
- [ ] 4
- [ ] 5
### 2021amc12b >12pxq
- [x] 1
- [x] 2
- [x] 3
- [x] 4
- [ ] 5
### 2021 aime1
- [x] 4
- [x] 5
- [x] 6
- [x] 7
- [x] 8
- [x] 9
- [ ] 10
- [ ] 11
- [ ] 12
- [ ] 13
### 2021 aime2
- [ ] 4
- [ ] 5
- [ ] 6
- [ ] 7
- [ ] 8
- [ ] 9
- [ ] 10
- [ ] 11
- [ ] 12
- [ ] 13

# notes
[[/plans]]
[[september3]]
![[prisms#schedule]]
[[prisms]]

##### Photosynthetic vs. photovoltaic efficiency (Blankenship et al., *Science*, 2011)

Comparing photosynthesis with solar panels is tricky because plants store energy in chemical bonds, while a PV cell produces electricity that isn't stored. The authors therefore compare photosynthesis with **PV-driven water electrolysis**, which also stores energy chemically. Splitting water takes almost exactly the same free energy (1.23 eV) as making carbohydrate (1.24 eV), so the two are a fair match.

###### Current efficiency

Efficiency here means the energy content of harvestable biomass divided by the total solar energy hitting the same area. It is measured over the whole solar spectrum.

| System | Efficiency |
|---|---|
| Crop plants, annual (temperate and tropical) | ≤1% |
| Microalgae in bioreactors, annual | ~3% |
| C3 plants, short-term peak growth | 3.5% |
| C4 plants, short-term peak growth | 4.3% |
| Microalgae, short-term (bubbled bioreactors) | ~5–7% |
| **PV + electrolysis benchmark, annual** | **~10–11%** |

The PV benchmark is built up as follows:
- Silicon modules convert about 18% at peak sun, and about 95% of that on an annual average.
- The electrolyzer is about 80% efficient, which gives roughly 14% overall.
- Voltage-mismatch losses then reduce this to about 10–11%.

Quantum efficiency is a separate measure: it is the fraction of absorbed photons that produce a stable product. For photosynthesis it is close to 100% under optimal conditions. The losses happen elsewhere.

###### Theoretical maximum

- **~12%** is the hard ceiling for making glucose from CO₂ and water. It is set by where chlorophyll's absorption ends and by the two-photosystem design.
- **4.6% (C3) and 6.0% (C4)** are the realistic maxima once unavoidable losses are included: light harvesting, overpotentials, and respiration.
- Short-term field efficiencies already reach **70–75%** of these realistic limits. Annual numbers fall much further below them, mostly because plants only grow for part of the year.

For comparison:
- A single-junction PV cell has a ceiling of about 32% (the Shockley–Queisser limit).
- About 24% is realistic for a photoelectrolysis cell.
- Tandem cells could approach 40%.
- Exotic designs such as hot-carrier and multi-carrier cells have a thermodynamic limit of 66%.

###### What limits photosynthesis

**Physics of light capture**
- **Narrow absorption window.** Pigments use only 400–700 nm, which is about half of incoming solar energy. Silicon absorbs out to about 1200 nm.
- **Heat loss from high-energy photons.** Blue light gets absorbed, but its extra energy is shed as heat down to the red absorption level. This is the same bandgap loss that PV cells have.
- **Two photosystems competing for the same light.** PSI and PSII work in series but absorb nearly the same wavelengths. Compared with an optimized tandem design, this cuts the energy efficiency nearly in half.

**Biochemistry**
- **Photorespiration.** RuBisCO sometimes grabs O₂ instead of CO₂, and the recovery process can consume up to 25% of stored energy. C4 plants and algae have CO₂-concentrating systems that largely avoid this, but those systems have their own energy cost.
- **Slow RuBisCO.** Because the enzyme is slow, plants must make huge amounts of it. That cost is part of a growth-and-maintenance overhead of at least 30% of stored energy.
- **"Legacy biochemistry."** Photosynthesis inherited redox chemistry from earlier non-photosynthetic organisms, and that chemistry isn't ideally matched to the job.

**Light management**
- **Oversized antennas.** In full sun, up to 80% of the energy absorbed by a leaf must be thrown away to avoid damage. Meanwhile, leaves lower in the canopy are starved for light.

**Environment and evolution**
- **CO₂ supply.** Dense crops can pull CO₂ inside the canopy 50 ppm or more below the surrounding air.
- **Mismatched regulation.** Plants evolved under pre-industrial CO₂ levels and don't fully take advantage of today's higher levels.
- **Wrong selection target.** Evolution selected plants for reproductive success, not biomass yield. Breeders selected for the harvested product, not overall efficiency.

###### Proposed fixes

**Near-term approaches:**
- Extend absorption into the near-infrared using chlorophyll variants that absorb at 740–750 nm.
- Shrink the light-harvesting antennas.
- Engineer C4 traits into C3 crops.
- Add a photorespiration bypass; one has been demonstrated in *Arabidopsis*.
- Feed algae flue gas, which is about 10% CO₂ and nearly eliminates photorespiration.

**The most ambitious idea:** re-engineer one photosystem to use bacteriochlorophyll that absorbs out to about 1100 nm. The two photosystems would then work as a true tandem cell, roughly doubling the number of photons captured. Other ideas include swapping in an alternative carbon-fixation cycle, or producing H₂ or formate directly instead of sugar.

###### Bottom line

On an annual basis, PV wins clearly: about 10–11% versus 1% or less for crops. Under ideal short-term conditions, however, photosynthesis comes within a factor of 2–3 of PV, and many of its losses could in principle be engineered out. Keep in mind this is a 2011 paper, so the PV and electrolyzer figures have improved since then. The photosynthesis limits and loss mechanisms are still the standard framework.
### sadge
I’m a student in Princeton, and I’m writing to respectfully urge Governor Sherrill to opt New Jersey into the new federal scholarship tax credit before the December 31 deadline. 

Starting in 2027, those who donate to approved scholarship organizations get a matching federal tax credit up to $1,700. The scholarships can pay for tutoring, special-needs services, books, and other school costs for students in public, private, and religious schools. Families earning up to three times the area median income qualify.

I will be frank that at least part of the reason this caught my attention was my own experience with public and private schools, such that I am generally inclined to side with school choice, as this smells of. However, you do not have to like school choice, or like Trump, the way this is rather partisan coded, as many things are. You just have to consider what is best for New Jersey.

Not opting in only funnels money from New Jersey out of state, especially New York, where governor Hochul, I should note a Democratic governor, has already decided to opt in. Anyone can still claim the tax credit even if Sherrill does not opt in, with the only difference being that the money no longer helps New Jersey students.

Princeton without doubt is an affluent town. With a high median household income of $184000, this tax credit is particularly relevant, as many families have sufficiently high tax burdens to make full use of it. If just 15 percent of Princeton’s roughly 9,000 households gave $1,700, that would be about $2.3 million a year. Without New Jersey opting in, all of it would fund students in other states.

Meanwhile, the need is right here. Princeton Public Schools has acknowledged gaps for lower-income students, English learners, and students in special education, which afflicts all districts. Scholarships could pay for tutoring for those same students, at no cost to the district.

The governor’s office has said it is weighing how the program could benefit public school students. In Princeton, the answer is concrete: math tutoring for a student whose family can’t afford it, or special-needs services for a child who needs them.

Skeptics associate opting in with Trump and school choice. They doubt that government money in education can be entrusted to private organiations. Supporting opting in is supporting neither. It is simply the obvious choice, given New Jersey taxpayers would regardless use the tax credit. The only difference is whether this helps New Jersey. Furthermore, federal law requires scholarship groups to verify family income, spend at least 90 percent of their money on scholarships, and never award scholarships to their own insiders, for example.

Lastly, I note that Governor Sherrill’s official residence is here in Princeton. As a Princeton-area neighbors, I ask her to say yes and keep our generosity working for New Jersey kids.

Steffan Pauwel
Lambert Dr, Princeton 08540
