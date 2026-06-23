# Method Card: Metodo del Gradiente con Line Search Esatta

- **Obiettivo**: Trovare il minimo non vincolato di $f(x)$.
- **Passi Operativi**:
  1. Calcolare il gradiente $\nabla f(x_k)$. Se $\|\nabla f(x_k)\| < \epsilon \implies$ Ottimo trovato.
  2. Impostare la direzione di discesa: $d_k = -\nabla f(x_k)$.
  3. Formulare la funzione di passo $\phi(\alpha) = f(x_k + \alpha d_k)$.
  4. Risolvere $\frac{d\phi(\alpha)}{d\alpha} = 0 \implies \alpha_k$ (passo esatto).
  5. Aggiornare il punto: $x_{k+1} = x_k + \alpha_k d_k$.
- **Proprietà Fondamentale**: Due direzioni consecutive sono ortogonali: $d_k^T d_{k-1} = 0$.
- **Esempio di Calcolo**: Vedi [[pnl_metodo_gradiente_line_search|Metodo Gradiente con LS]] o [[pnl_esercizi_non_vincolati|Esempio Gradiente Svolto]].
