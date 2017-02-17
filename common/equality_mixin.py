'''
Contains EqualityMixin
'''
class EqualityMixin(object):
    '''This Mixin Allows operation to compare class elements'''
    def __eq__(self, other):
        '''Override the default Equals behavior'''
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        '''Override the default Not-Equals behavior'''
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented
