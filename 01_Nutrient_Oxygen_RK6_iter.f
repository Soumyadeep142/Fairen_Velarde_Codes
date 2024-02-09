      implicit double precision(a-h, o-z)
      DOUBLE PRECISION k1a, k2a, k3a, k4a, k5a, k6a
      DOUBLE PRECISION k1b, k2b, k3b, k4b, k5b, k6b
      DOUBLE PRECISION a,b,dk,x,y,t,delx,dely,z, t_ini
      DOUBLE PRECISION term3a, term3b, term4a, term4b
      DOUBLE PRECISION term5a, term5b, term6a, term6b
      INTEGER i, iter
      character(len=10) :: iter_str
      include 'params.inc'
c     For N no of configurations            
      do 7 iter=1,no_of_confg 
      write(iter_str, '(I0)') iter
      write(*,*) iter
      open(8, file='time_N_O_data_'//trim(adjustl(iter_str))//'.txt') 
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
      	z=rand()*width-0.5*width
	
        k1a=h*f(z,x,y,t,a,b,dk)
        k1b=h*g(z,x,y,t,a,b,dk)

        k2a=h*f(z,x+0.25*k1a, y+0.25*k1b, t+0.25*h,a,b,dk)
        k2b=h*g(z,x+0.25*k1a, y+0.25*k1b, t+0.25*h,a,b,dk)
       
        term3a=3.*k1a/32.+9.*k2a/32.
        term3b=3.*k1b/32.+9.*k2b/32.
        k3a=h*f(z,x+term3a,y+term3b,t+3.*h/8.,a,b,dk)
        k3b=h*g(z,x+term3a,y+term3b,t+3.*h/8.,a,b,dk)
      
        term4a=1932.*k1a/2197.-7200.*k2a/2197.+7296.*k3a/2197.
        term4b=1932.*k1b/2197.-7200.*k2b/2197.+7296.*k3b/2197.
        k4a=h*f(z,x+term4a, y+term4b, t+12.*h/13.,a,b,dk)
        k4b=h*g(z,x+term4a, y+term4b, t+12.*h/13.,a,b,dk)
      
        term5a=439.*k1a-8.*k2a+3680.*k3a/513.-845.*k4a/4104.
        term5b=439.*k1b-8.*k2b+3680.*k3b/513.-845.*k4b/4104.
        k5a=h*f(z,x+term5a, y+term5b, t+h,a,b,dk)
        k5b=h*g(z,x+term5a, y+term5b, t+h,a,b,dk)
      
        term6a=-8.*k1a/27.+2.*k2a-3544./2565.*k3a+1859./4104.*k4a-11*k5a/40.
        term6b=-8.*k1b/27.+2.*k2b-3544./2565.*k3b+1859./4104.*k4b-11*k5b/40.
        k6a=h*f(z,x+term6a, y+term6b, t+h/2.,a,b,dk)
        k6b=h*g(z,x+term6a, y+term6b, t+h/2.,a,b,dk)
      
        delx=16/135*k1a+6656/12823*k3a+28561./56430.*k4a-9*k5a/50.+2*k6a/55.
        dely=16/135*k1b+6656/12823*k3b+28561./56430.*k4b-9*k5b/50.+2*k6b/55.
      	x=x+delx
      	y=y+dely
 39   continue
      close(8)
 7    continue
      stop
      end
      
      
      double precision function f(z1,x,y,t,a,b,dk)
      implicit double precision(a-h, o-z)
      DOUBLE PRECISION a,b,dk,z1
      f=a-x-x*y/(1+dk*x*x)+z1
      return
      end
      
      double precision function g(z2,x,y,t,a,b,dk)
      implicit double precision(a-h, o-z)
      DOUBLE PRECISION a,b,dk,z2
      g=b-x*y/(1+dk*x*x)+z2
      return
      end
