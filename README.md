# BaskeAnaTool
1.When firstly use this package, please: 

   ` source ./setup.sh`


2.A basket of analysis codes, contains:
 - A) sub jobs:
   - BOSS jobs:

     `Hepsub -txt [-r] [path]`

   - Bash jobs:

     `Hepsub -sh [-r] [path] `

   - ROOT jobs

     `Hepsub -c [-r] [path]`
 
 - B) make jobs, only the reconstruction and simulation jobs can be made
  - usage

  `SimJpsi [decay.card] [number of events]`

  - different type
   - Sim3770 
   - SimNewJpsi
   - SimJpsi
   - Sim4180
   

