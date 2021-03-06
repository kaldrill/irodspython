# Copyright (c) 2013, University of Liverpool
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Author       : Jerome Fuselier
#

import unittest
from common import *
from irods import *

class testRodsXmsg(iRODSTestCase):

    def test_getXmsgTicketInp_t(self):
        v1 = create_getXmsgTicketInp_t()
        v2 = create_getXmsgTicketInp_t()
        self.assertTrue(test_getXmsgTicketInp_t(v1, v2))

    def test_rcvXmsgInp_t(self):
        v1 = create_rcvXmsgInp_t()
        v2 = create_rcvXmsgInp_t()
        self.assertTrue(test_rcvXmsgInp_t(v1, v2))
 
    def test_rcvXmsgOut_t(self):
        v1 = create_rcvXmsgOut_t()
        v2 = create_rcvXmsgOut_t()
        self.assertTrue(test_rcvXmsgOut_t(v1, v2))
 
    def test_xmsgTicketInfo_t(self):
        v1 = create_xmsgTicketInfo_t()
        v2 = create_xmsgTicketInfo_t()
        self.assertTrue(test_xmsgTicketInfo_t(v1, v2))
 
    def test_sendXmsgInp_t(self):
        v1 = create_sendXmsgInp_t()
        v2 = create_sendXmsgInp_t()
        self.assertTrue(test_sendXmsgInp_t(v1, v2))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testRodsXmsg))
    
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
