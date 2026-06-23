# Flashcard Programmazione Non Lineare Vincolata (KKT)

#flashcards/pnl/vincolata-kkt

## Q: Quali sono le condizioni KKT per un problema di minimo $\min f(x)$ s.t. $g_i(x)=0, h_j(x) \le 0$?
A: 
1. **Stazionarietà**: $\nabla f(x^*) + \sum \lambda_i^* \nabla g_i(x^*) + \sum \mu_j^* \nabla h_j(x^*) = 0$
2. **Ammissibilità Primale**: $g_i(x^*) = 0, \quad h_j(x^*) \le 0$
3. **Ammissibilità Duale**: $\mu_j^* \ge 0$
4. **Complementarità**: $\mu_j^* \cdot h_j(x^*) = 0$
<!-- Estensione: Rop-PNL-CondizioniKKT -->

## Q: Come varia il segno dei moltiplicatori $\mu_j$ nelle condizioni KKT per un problema di massimo ($\max f(x)$ s.t. $h_j(x) \le 0$)?
A: Per problemi di massimo, i moltiplicatori dei vincoli attivi in forma standard devono essere non positivi:
$$\mu_j^* \le 0$$
<!-- Estensione: Rop-PNL-KKTMaxSegno -->

## Q: Con un vincolo di uguaglianza $g_i(x) = 0$, il moltiplicatore ha vincolo di segno?
A: No, il moltiplicatore lagrangiano $\lambda_i$ associato ad un vincolo di uguaglianza è libero in segno ($\lambda_i \in \mathbb{R}$).
<!-- Estensione: Rop-PNL-LagrangeSegno -->

## Q: Cosa significa che un vincolo di disuguaglianza $h_j(x) \le 0$ è "attivo" o "inattivo" in un punto ammissibile $x^*$?
A: 
- **Attivo**: se $h_j(x^*) = 0$. Il punto giace sul bordo del vincolo; il moltiplicatore $\mu_j^*$ può essere non nullo.
- **Inattivo**: se $h_j(x^*) < 0$. Il punto giace all'interno del semispazio ammissibile; per complementarità si ha necessariamente $\mu_j^* = 0$.
<!-- Estensione: Rop-PNL-VincoloAttivoInattivo -->

## Q: Quante combinazioni di vincoli attivi e inattivi devono essere esplorate in presenza di $p$ vincoli di disuguaglianza?
A: Si devono esplorare $2^p$ combinazioni di casi possibili analizzando singolarmente ciascun caso per complementarità degli scarti.
<!-- Estensione: Rop-PNL-CombinatoriaKKT -->
