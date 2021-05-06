class Task(object):
    def __init__(self, subTask, subTask_calculatedAmount, subTask_dependencyRelationship, subTask_dataDependency):
        '''

        :param subTask: n dimension list
        :param subTask_calculatedAmount: n dimension list
        :param subTask_dependencyRelationship: n*n matrix
        :param subTask_dataDependency: n*n matrix
        '''
        self.subTask = subTask
        self.subTask_calculatedAmount = subTask_calculatedAmount
        self.subTask_dependencyRelationship = subTask_dependencyRelationship
        self.subTask_dataDependency = subTask_dataDependency


