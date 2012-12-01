from django.test import TestCase
from django.db import IntegrityError
from binder import models

class ModelTests(TestCase):
    def test_EmptyBindServerModel(self):
        """Test that adding a well-formed BindServer works."""
        self.assertEqual(models.BindServer.objects.count(), 0)
        bindserver_1 = models.BindServer(hostname="test1",
                                        statistics_port=1234)
        bindserver_1.save()
        self.assertEqual(models.BindServer.objects.count(), 1)

    def test_BindServerMissingStatisticsPort(self):
        """Attempt to add a BindServer without a statistics port."""
        bindserver_1 = models.BindServer(hostname="badtest1")
        with self.assertRaisesMessage(IntegrityError, "binder_bindserver.statistics_port may not be NULL"):
            bindserver_1.save()

    def test_BindServerNonIntStatisticsPort(self):
        """Attempt to add a Bindserver with a non-integer statistics port."""
        bindserver_1 = models.BindServer(hostname="foo",
                                         statistics_port="bar1")
        with self.assertRaisesMessage(ValueError, "invalid literal for int() with base 10: 'bar1'"):
            bindserver_1.save()