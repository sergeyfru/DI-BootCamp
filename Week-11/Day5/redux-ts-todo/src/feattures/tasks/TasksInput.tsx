import { useRef, memo } from "react"
import { useAddTask } from "./hooks"

const TasksInput = () => {
    console.log('TaskInput Render');
    
    const inputRef = useRef<HTMLInputElement>(null)
    const addTaskHook = useAddTask();

    const addTask = () => {
        const task: string = inputRef.current?.value.trim() || '';
        if(task === '') return
        addTaskHook(task)
        inputRef.current!.value = ""
    }

    return (
        <>
            <div>
                <input type="text" ref={inputRef} />
                <button onClick={addTask}>Add Task</button>
            </div>
        </>
    )
}

const MemorizedTaskInput = memo(TasksInput)
export default MemorizedTaskInput