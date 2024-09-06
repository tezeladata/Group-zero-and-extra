export default function Grid(){
    return(
        <section className="grid grid-cols-3 grid-rows-5 gap-5 h-screen w-screen p-5">
            <div className="col-start-1 col-end-2 row-start-1 row-end-2 grid grid-cols-4 grid-rows-5 gap-0.5">
                <div className="col-start-1 col-end-2 row-start-1 row-end-2 bg-cyan-600 flex items-center justify-center">Percussion, 2</div>
                <div className="col-start-1 col-end-2 row-start-2 row-end-6 bg-red-400 flex items-center justify-center">Brass, 2</div>
                <div className="col-start-2 col-end-3 row-start-1 row-end-6 bg-green-600 flex items-center justify-center">Woodwinds, 2</div>
                <div className="col-start-3 col-end-5 row-start-1 row-end-6 bg-yellow-500 flex items-center justify-center">Strings, 2</div>
            </div>

            <div className="col-start-1 col-end-2 row-start-2 row-end-6 grid grid-cols-3 grid-rows-5 gap-0.5">
                <div className="row-start-1 row-end-3 col-start-1 col-end-2 bg-cyan-600 flex items-center justify-center">Percussion, 1</div>
                <div className="row-start-1 row-end-3 col-start-2 col-end-3 bg-red-400 flex items-center justify-center">Brass, 1</div>
                <div className="row-start-1 row-end-3 col-start-3 col-end-4 bg-green-600 flex items-center justify-center">Woodwinds, 2</div>
                <div className="row-start-3 row-end-6 col-start-1 col-end-4 bg-yellow-500 flex items-center justify-center">Strings, 6</div>
            </div>

            <div className="col-start-2 col-end-4 row-start-1 row-end-3 grid grid-cols-7 grid-rows-7 gap-0.5">
                <div className="col-start-1 col-end-2 row-start-1 row-end-2 bg-purple-500 flex items-center justify-center">Keyboards, 1</div>
                <div className="col-start-1 col-end-2 row-start-2 row-end-8 bg-cyan-600 flex items-center justify-center">Percussion, 1</div>
                <div className="col-start-2 col-end-4 row-start-1 row-end-4 bg-green-600 flex items-center justify-center">Woodwinds, 3</div>
                <div className="col-start-2 col-end-4 row-start-4 row-end-8 bg-red-400 flex items-center justify-center">Brass, 1</div>
                <div className="col-start-4 col-end-8 row-start-1 row-end-8 bg-yellow-500 flex items-center justify-center">Strings, 14</div>
            </div>

            <div className="col-start-2 col-end-4 row-start-3 row-end-6 grid grid-cols-7 grid-rows-7 gap-0.5">
                <div className="col-start-1 col-end-2 row-start-1 row-end-2 bg-purple-500 flex items-center justify-center">Keyboards, 1</div>
                <div className="col-start-1 col-end-2 row-start-2 row-end-8 bg-cyan-600 flex items-center justify-center">Percussion, 1</div>
                <div className="col-start-2 col-end-4 row-start-1 row-end-4 bg-green-600 flex items-center justify-center">Woodwinds, 4</div>
                <div className="col-start-2 col-end-4 row-start-4 row-end-8 bg-red-400 flex items-center justify-center">Brass, 2</div>
                <div className="col-start-4 col-end-8 row-start-1 row-end-8 bg-yellow-500 flex items-center justify-center">Strings, 16</div>
            </div>
        </section>
    )
}