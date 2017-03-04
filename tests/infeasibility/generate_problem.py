import scipy.sparse as spa
import scipy as sp
import utils.codegen_utils as cu


n = 50
m = 150

# Generate random Matrices
Pt = spa.random(n, n)
P = Pt.T.dot(Pt).tocsc() + spa.eye(n)
q = sp.randn(n)
A = spa.random(m, n).tolil()  # Lil for efficiency
u = 3 + sp.randn(m)
l = -3 + sp.randn(m)

# Make random problem infeasible
A[int(n/2), :] = A[int(n/2)+1, :]
l[int(n/2)] = u[int(n/2)+1] + 10 * sp.rand()
u[int(n/2)] = l[int(n/2)] + 0.5

# Convert A to csc
A = A.tocsc()

# Generate problem solutions
sols_data = {'status_test': 'infeasible'}


# Generate problem data
cu.generate_problem_data(P, q, A, l, u, 'infeasibility', sols_data)
