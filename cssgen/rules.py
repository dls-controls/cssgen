import xml.etree.ElementTree as et
from opimodel import rules


class OpiRuleRenderer(object):

    def render(self, rules_node, rule_list):
        for rule_model in rule_list:
            self.render_one(rules_node, rule_model)

    def render_one(self, rules_node, rule_model):
        self.rule_node = et.SubElement(rules_node, 'rule')
        self.rule_node.set('prop_id', rule_model._prop_id)
        self.rule_node.set('name', 'Rule')
        if isinstance(rule_model, rules.BetweenRule):
            self.render_between(rule_model)
        elif isinstance(rule_model, rules.GreaterThanRule):
            self.render_greater_than(rule_model)

    def render_between(self, rule_model):
        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = rule_model._pv
        exp_node1 = et.SubElement(self.rule_node, 'exp')
        exp_node1.set('bool_exp', 'pv0 < {}'.format(rule_model._min))
        val_node1 = et.SubElement(exp_node1, 'value')
        val_node1.text = 'false'
        exp_node2 = et.SubElement(self.rule_node, 'exp')
        exp_node2.set('bool_exp', 'pv0 > {}'.format(rule_model._max))
        val_node2 = et.SubElement(exp_node2, 'value')
        val_node2.text = 'false'
        exp_node3 = et.SubElement(self.rule_node, 'exp')
        exp_node3.set('bool_exp', 'true')
        val_node3 = et.SubElement(exp_node3, 'value')
        val_node3.text = 'true'

    def render_greater_than(self, rule_model):
        pv_node = et.SubElement(self.rule_node, 'pv')
        pv_node.set('trig', 'true')
        pv_node.text = rule_model._pv
        exp_node1 = et.SubElement(self.rule_node, 'exp')
        exp_node1.set('bool_exp', 'pv0 > {}'.format(rule_model._threshold))
        val_node1 = et.SubElement(exp_node1, 'value')
        val_node1.text = 'true'
        exp_node2 = et.SubElement(self.rule_node, 'exp')
        exp_node2.set('bool_exp', 'true')
        val_node2 = et.SubElement(exp_node2, 'value')
        val_node2.text = 'false'
