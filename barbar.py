from constants import *
from text_formatting import *

class Solver():
  def __init__(self, in_file):
    self._read_in_file(in_file)

  def _read_in_file(self, in_file):
    with open(att_path + in_file) as f:
      RC = f.readline().split(' ')
      try:
        R = int(RC[0])
      except ValueError:
        raise ValueError(R_NU_E_INT) 
      if R < MIN_NR:
        raise Exception(R_ESTE_MAI_MIC_CA_1)
      if R > MAX_NR:
        raise Exception(R_ESTE_MAI_MARE_CA_1000)

      try:
        C = int(RC[1])
      except ValueError:
        raise ValueError(C_NU_E_INT)
      
      if C < MIN_NR:
        raise Exception(C_ESTE_MAI_MIC_CA_1)
      if C > MAX_NR:
        raise Exception(C_ESTE_MAI_MARE_CA_1000)

      viz = [[False]*C for i in range(R)]
      dist = [[None]*C for i in range(R)]
      q = [] # empty queue
      I = None
      O = None
      string_map = f.readlines()

    if len(string_map) != R:
      raise Exception(fis_nu_are_linii(R))

    for i in range(R):
      if len(string_map[i]) != C + 1:
        raise Exception(linia_nu_are_caract(i, C))
      for j in range(C):
        if string_map[i][j] == '.':
          pass
        elif string_map[i][j] == 'D':
          dist[i][j] = 0
          q.append((i, j))
          viz[i][j] = True
        elif string_map[i][j] == 'I':
          I = (i, j)
        elif string_map[i][j] == '*':
          dist[i][j] = None
          viz[i][j] = True
        elif string_map[i][j] == 'O':
          O = (i, j)
        else:
          raise Exception(caract_nu_e_permis(string_map[i][j]))

    if I is None:
      raise Exception(NO_I)

    if O is None:
      raise Exception(NO_O)

    self.viz = viz
    self.dist = dist
    self.I = I
    self.O = O
    self.q = q
    self.R = R
    self.C = C


  def _get_dragons_dist(self):
    print(len(self.q))
    if len(self.q) == 0:
      raise Exception(NU_SUNT_DRAGONI)
    
    while len(self.q) != 0:
      curr = self.q[0]

      for p in range(4):
        
        i = curr[0] + ROW[p]
        j = curr[1] + COL[p]

        if self.R > i >= 0 and self.C > j >= 0 and not self.viz[i][j]:
          self.dist[i][j] = self.dist[curr[0]][curr[1]] + 1
          self.viz[i][j] = True
          self.q.append((i, j))
      
      self.q.pop(0)


  def _bfs_cond(self, i, j, x):
    return self.R > i >= 0 and self.C > j >= 0 and not self.viz[i][j] and self.dist[i][j] is not None and self.dist[i][j] >= x

  def _bfs(self, x):
    I = self.I
    O = self.O
    self.viz = [[False] * self.C for i in range(self.R)]
    q = [I]
    
    if self.dist[I[0]][I[1]] < x:
      return False

    while len(q) != 0 and not self.viz[O[0]][O[1]]:
      curr = q[0]
      for p in range(4):
        i = curr[0] + ROW[p]
        j = curr[1] + COL[p]

        if self._bfs_cond(i, j, x):
          self.viz[i][j] = True
          q.append((i, j))
      
      q.pop(0)

    return self.viz[O[0]][O[1]]
  

  def _binary_search(self, st, dr):
    while st <= dr:
      mid = (st + dr) // 2
      if not self._bfs(mid):
        dr = mid - 1
      else:
        st = mid + 1
    
    return dr


  def solve(self):
    self._get_dragons_dist()
    self.answer = self._binary_search(1, max(self.R, self.C))
    if self.answer == 0:
      self.answer = -1
    
    return self.answer


def get_output(out_file):
  with open(att_path + out_file) as f:
    line = f.readline().strip()
  try:
    ground_truth = int(line)
    return ground_truth
  except ValueError:
    raise ValueError(nu_este_numar(line))  

# if __name__ == '__main__':
  
#   file_name = 'no_dragons.in'

#   solver = Solver(file_name)
#   solver.solve()
#   print(solver.answer)
    
#   ground_truth = get_output('grader_test1.ok')
#   print(solver.answer == ground_truth)

#   print(solver.answer)


  












