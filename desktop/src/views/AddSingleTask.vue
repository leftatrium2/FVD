<template>
  <div class="task-container">
    <h1>{{ $t('addTask.singleTitle') }}</h1>
    <el-form label-width="120px">
      <el-form-item label="Video URL">
        <el-input placeholder="Please enter video URL" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary">Add Task</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
