from functools import reduce

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Task, Bucket

class TaskTest(APITestCase):
    def __init__(self, *args, **kwargs):
        """
        initializing custom attributes 
        and calling parent class constructor to avioid test breaks
        """
        super().__init__(*args, **kwargs)
        self.bucket_list = []

    def test_task_list(self, task_len=0):
        """test case for list of tasks

        Args:
            task_len (int, optional): expected length of the task list. Defaults to 0.
        """
        response = self.client.get('/tasks')
        self.assertEqual(len(response.data), task_len)

    def test_create_bucket(self):
        """test case to create a new bucket
        """
        data = {'name': "office works"}
        response = self.client.post('/buckets', data) 
        bk_response = self.client.get('/buckets')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(bk_response.data), 1) 

    def test_create_task(self):
        """test case to create a task under a bucket
        """
        self.test_create_bucket()
        bucket = Bucket.objects.first()
        data = {'title': 'meeting at 9pm tonight', 'bucket_id': bucket.id}
        tk_response = self.client.post('/tasks', data)  
        self.assertEqual(tk_response.status_code, status.HTTP_201_CREATED)
        self.test_task_list(len(tk_response.data))

    def test_update_task(self):
        """testcase to update a task,\n 
           here we update first task status 'is_done' to True
        """
        self.test_create_task()
        task = Task.objects.get(id=1)
        tk_response = self.client.put(f'/task/{task.id}', {'is_done': True})
        self.assertEqual(tk_response.status_code, status.HTTP_200_OK)
        updated_task = Task.objects.get(id=1)
        self.assertEqual(updated_task.is_done, True)

    def test_delete_task(self):
        """testcase to check delete operation of a task.
        """
        self.test_create_task()
        task = Task.objects.get(id=1)
        self.assertEqual(Task.objects.count(), 1)
        tk_response = self.client.delete(f'/task/{task.id}')
        self.assertEqual(tk_response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 0)


