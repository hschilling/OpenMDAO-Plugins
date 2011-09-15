.. index:: NLPQ plugin overview

Overview of the NLPQ Plugin
==============================

The NLPQ Plugin is a wrapper for the NLPQL Fortran source code written by 
`Prof. Klaus Schittkowski
<http://www.klaus-schittkowski.de/>`_
of the University of Bayreuth. This source code was given to 
Dr. Les Berke, retired Branch Chief in Structures and Materials Division, of 
the NASA Glenn Research Center in the mid-1990's.

The NLPQL code is a Fortran subroutine for solving constrained nonlinear programming problems. For more information see

K. Schittkowski (1985/86): NLPQL: A FORTRAN subroutine solving constrained nonlinear programming problems, Annals of Operations Research, Vol. 5, 485-500

The rest of this document assumes that you have already installed OpenMDAO and understand
some of the basics of using OpenMDAO.

This document also assumes that the user has some understanding of how NLPQ
works. For more information about NLPQ, the only reliable source is the source
code itself in nlpq.f.

.. note::  This plugin is only intended for use
           at the NASA Glenn Research Center since it was 
           the NLPQ Fortran code was only given for use
           at the Center.

.. note::  Currently it has only been tested on Linux.


How Do I Use the NLPQ Plugin?
-------------------------------------

Using the plugin is like using other optimizer drivers available in 
OpenMDAO. 

Here is some example code. The comments explain some details of the usage of this
component.

.. testcode:: NLPQdriver

    import numpy
    
    from openmdao.main.api import Assembly, Component, set_as_top
    from openmdao.lib.datatypes.api import Array, Float
    
    from nlpqdriver.nlpqdriver import NLPQdriver
    
    
    class ParaboloidComponent(Component):
        """     
             MINIMIZE OBJ = ( X(1) - 2.0 ) ** 2 +  ( X(2) - 3.0 ) **2
        """
        
        x = Array(iotype='in', low=-1e99, high=1e99)
        result = Float(iotype='out')
        
        def __init__(self, doc=None):
            super(ParaboloidComponent, self).__init__(doc)
            self.x = numpy.array([10., 10.], dtype=float) # initial guess
            self.result = 0.
            
            self.opt_objective = 0.
            self.opt_design_vars = [2., 3.]
    
        def execute(self):
            """calculate the new objective value"""
            
            self.result = (self.x[0] - 2.0) ** 2 + (self.x[1] - 3.0) ** 2
    
    top = set_as_top(Assembly())
    top.add('comp', ParaboloidComponent())
    top.add('driver', NLPQdriver())
    top.driver.workflow.add('comp')
    top.driver.itmax = 30
    top.driver.iprint = 0
    
    top.driver.add_objective( 'comp.result' )
    map(top.driver.add_parameter, 
        ['comp.x[0]', 'comp.x[1]',])
    top.driver.lower_bounds = [-100.0, -100.0]
    top.driver.upper_bounds = [ 100.0,  100.0]
    
    map(top.driver.add_constraint,[ 'comp.x[0] - 4.0 > 0.0' ] )

    top.run()
    
    print "%.4f %.4f %.4f" % ( top.comp.x[0], top.comp.x[1], top.driver.eval_objective() )

    
.. testoutput:: NLPQdriver
   :hide:
   :options: -ELLIPSIS, +NORMALIZE_WHITESPACE

   4.0000 3.0000 4.0000