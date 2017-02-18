'''
Created on Feb 15, 2017

@author: julien
'''
import unittest


from minos.experiment.experiment import Experiment, ExperimentParameters
from minos.experiment.training import Training
from minos.model.design import create_random_blueprint, mutate_blueprint
from minos.model.model import Layout


class MutationTest(unittest.TestCase):

    def test_mutate_layout(self):
        layout = Layout(
            input_size=100,
            output_size=10,
            output_activation='softmax')
        training = Training(
            objective=None,
            optimizer=None,
            metric=None,
            stopping=None,
            batch_size=None)
        experiment = Experiment(
            'test',
            layout,
            training,
            batch_iterator=None,
            test_batch_iterator=None,
            environment=None,
            parameters=ExperimentParameters(use_default_values=False))
        for _ in range(50):
            blueprint = create_random_blueprint(experiment)
            mutant = mutate_blueprint(
                blueprint,
                parameters=experiment.parameters,
                p_mutate_layout=1,
                layout_mutation_count=1,
                layout_mutables=['rows'],
                mutate_in_place=False)
            self.assertTrue(
                len(mutant.layout.rows) != len(blueprint.layout.rows),
                'Should have mutated rows')
            mutant = mutate_blueprint(
                blueprint,
                parameters=experiment.parameters,
                p_mutate_layout=1,
                layout_mutation_count=1,
                layout_mutables=['blocks'],
                mutate_in_place=False)
            self.assertTrue(
                len(mutant.layout.get_blocks()) != len(blueprint.layout.get_blocks()),
                'Should have mutated blocks')
            mutant = mutate_blueprint(
                blueprint,
                parameters=experiment.parameters,
                p_mutate_layout=1,
                layout_mutation_count=1,
                layout_mutables=['layers'],
                mutate_in_place=False)
            self.assertTrue(
                len(mutant.layout.get_layers()) != len(blueprint.layout.get_layers()),
                'Should have mutated layers')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
