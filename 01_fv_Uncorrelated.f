      implicit double precision(a-h, o-z)
      DOUBLE PRECISION k1a, k2a, k3a, k4a, k5a, k6a
      DOUBLE PRECISION k1b, k2b, k3b, k4b, k5b, k6b
      DOUBLE PRECISION a,b,dk,x,y,t,delx,dely,z, t_ini
      DOUBLE PRECISION term3a, term3b, term4a, term4b
      DOUBLE PRECISION term5a, term5b, term6a, term6b
      DOUBLE PRECISION new_width, z1, z2
      INTEGER i, iter, folderIndex, unitNumber
      character(len=10) :: iter_str
      INTEGER :: status
      CHARACTER(LEN=:), ALLOCATABLE :: folderName, fileName

      include 'params.inc'
      character(len=50) :: folder_name

c     For N no of configurations
      open(11, file='noise_data_2.txt')
      DO 44 folderIndex = 1, 9
      folderName = 'F_'//TRIM(ADJUSTL(ACHAR(IACHAR('0')+folderIndex)))

      CALL MKDIR(folderName, status)
      new_width=width+(folderIndex-1)*0.1
      write(11,*)folderIndex, new_width
      do 7 iter=1,no_of_confg 
      write(iter_str, '(I0)') iter
c      write(*,*) iter
      
      filename=trim(folderName)//'/t_'//trim(adjustl(iter_str))//'.txt'
      open(8, file=filename)
c    Giving the initial values
      a=alpha
      b=beta
      dk=kappa
      x=3.d0
      y=1.d0
      t_ini=lower_time
      t=t_ini
      do 39 i=1,time_division+1
c    Writing the file; diff denotes the time gap
        if (mod(i-1,diff).eq.0) then
        	write(8,*) t, x, y
        endif
        t=t_ini+(i-1)*h
c      	write(*,*) t
c       Giving the initial noise, change the width in params.inc file for different noise      	
      	z1=rand()*new_width-0.5*new_width
	z2=rand()*new_width-0.5*new_width
	
        k1a=h*f(z1,z2,x,y,t,a,b,dk)
        k1b=h*g(z1,z2,x,y,t,a,b,dk)

        k2a=h*f(z1,z2,x+0.25*k1a, y+0.25*k1b, t+0.25*h,a,b,dk)
        k2b=h*g(z1,z2,x+0.25*k1a, y+0.25*k1b, t+0.25*h,a,b,dk)
       
        term3a=3.*k1a/32.+9.*k2a/32.
        term3b=3.*k1b/32.+9.*k2b/32.
        k3a=h*f(z1,z2,x+term3a,y+term3b,t+3.*h/8.,a,b,dk)
        k3b=h*g(z1,z2,x+term3a,y+term3b,t+3.*h/8.,a,b,dk)
      
        term4a=1932.*k1a/2197.-7200.*k2a/2197.+7296.*k3a/2197.
        term4b=1932.*k1b/2197.-7200.*k2b/2197.+7296.*k3b/2197.
        k4a=h*f(z1,z2,x+term4a, y+term4b, t+12.*h/13.,a,b,dk)
        k4b=h*g(z1,z2,x+term4a, y+term4b, t+12.*h/13.,a,b,dk)
      
        term5a=439.*k1a-8.*k2a+3680.*k3a/513.-845.*k4a/4104.
        term5b=439.*k1b-8.*k2b+3680.*k3b/513.-845.*k4b/4104.
        k5a=h*f(z1,z2,x+term5a, y+term5b, t+h,a,b,dk)
        k5b=h*g(z1,z2,x+term5a, y+term5b, t+h,a,b,dk)
      
        term6a=-8.*k1a/27.+2.*k2a-3544./2565.*k3a+1859./4104.*k4a-11*k5a/40.
        term6b=-8.*k1b/27.+2.*k2b-3544./2565.*k3b+1859./4104.*k4b-11*k5b/40.
        k6a=h*f(z1,z2,x+term6a, y+term6b, t+h/2.,a,b,dk)
        k6b=h*g(z1,z2,x+term6a, y+term6b, t+h/2.,a,b,dk)
      
        delx=16/135*k1a+6656/12823*k3a+28561./56430.*k4a-9*k5a/50.+2*k6a/55.
        dely=16/135*k1b+6656/12823*k3b+28561./56430.*k4b-9*k5b/50.+2*k6b/55.
      	x=x+delx
      	y=y+dely
 39   continue
      close(8)
 7    continue
 44   continue
      stop
      end
      
      
      double precision function f(z1,z2,x,y,t,a,b,dk)
      implicit double precision(a-h, o-z)
      DOUBLE PRECISION a,b,dk,z1,z2
      f=a-x-x*y/(1+dk*x*x)+z1
      return
      end
      
      double precision function g(z1,z2,x,y,t,a,b,dk)
      implicit double precision(a-h, o-z)
      DOUBLE PRECISION a,b,dk,z1,z2
      g=b-x*y/(1+dk*x*x)+z2
      return
      end

      SUBROUTINE MKDIR(folderName, status)
        CHARACTER(LEN=*), INTENT(IN) :: folderName
        INTEGER, INTENT(OUT) :: status
      CALL SYSTEM('mkdir -p "' // TRIM(folderName) // '"')
      status = 0
      END SUBROUTINE MKDIR
