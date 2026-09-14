# The turkey problem revisited

**What dimensional analysis can and cannot decide**

l0d0v1c, pseudoLucV7

A classic dimensional-analysis exercise asks: *if a 5 lb turkey takes five
hours to roast, how long does a 10 lb turkey take?* The textbook answer is
$t \propto m^{2/3}$, or about 8 hours. This note looks at what is wrong with
that exercise.

- **The data are made up.** Published roasting charts give about 3 hours for a
  10 lb bird, not 5 or 8.
- **The $2/3$ law does not come from dimensional analysis alone.** It follows
  from one modelling choice among several. If you list the variables
  carelessly (both $\alpha$ and $k, \rho, c$; both $m$ and $l$), you get
  sixteen admissible formulae that reduce to six. Ten of them contain the
  absolute temperature $T$, which the linear heat equation cannot contain.
  Set up correctly, the problem gives a single group,
  $\mathrm{Fo} = t\alpha/l^2 = F(\mathrm{Bi}, \theta)$.
- **Correlation coefficients cannot choose between exponents.** A weighted
  log–log regression on the chart data gives $n = 0.54 \pm 0.02$. This rules
  out $n = 1$ at $7.5\sigma$ and is below $2/3$.
- **A finite Biot number explains the gap.** For realistic oven heat-transfer
  coefficients, the model gives $n_\text{eff} = 0.54$–$0.60$. The measured
  exponent therefore supports the diffusive model rather than contradicting
  it.

The paper ends with a corrected version of the exercise.

## Contents

| File          | Description                                  |
|---------------|----------------------------------------------|
| `turkey3.tex` | LaTeX source of the paper                    |
| `turkey3.pdf` | Compiled paper                               |
| `fig.py`      | Script that generates Figure 1               |
| `fig1.pdf`    | Figure 1                                     |

Figure 1 has three panels:
- **(a)** Roasting-chart data (stuffed and unstuffed) on log–log axes, with
  the fit and the $n = 2/3$ and $n = 1$ reference lines.
- **(b)** $r(m^x, t)$ as a function of the assumed exponent $x$. It varies by
  less than 0.004 over the whole range.
- **(c)** Effective exponent as a function of the Biot number, from the
  one-term series solution for a sphere.

## Reproducing

Figure (requires Python with `numpy`, `scipy` and `matplotlib`):

```sh
python fig.py        # writes fig1.pdf
```

Paper (requires a LaTeX distribution with `siunitx`, `booktabs` and
`hyperref`):

```sh
pdflatex turkey3.tex
pdflatex turkey3.tex
```
