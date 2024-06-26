C params.inc
      INTEGER, PARAMETER :: no_of_confg = 1000
      DOUBLE PRECISION, PARAMETER :: alpha = 19.4
      DOUBLE PRECISION, PARAMETER :: beta = 10.997
      DOUBLE PRECISION, PARAMETER :: kappa = 0.374
      DOUBLE PRECISION, PARAMETER :: upper_time = 10000.0
      DOUBLE PRECISION, PARAMETER :: lower_time = 0.0
      DOUBLE PRECISION, PARAMETER :: h = 0.001
      INTEGER, PARAMETER :: time_division = INT(upper_time / h)
      DOUBLE PRECISION, PARAMETER :: width = 0.6
      INTEGER, PARAMETER :: diff = 1000
      DOUBLE PRECISION, PARAMETER :: confg = no_of_confg*1.d0
      DOUBLE PRECISION, PARAMETER :: rho = 0.2
