import chess
from chessEng import Eng
import chess.engine
import asyncio


async def main() -> None:
    board = chess.Board()
    myEng = Eng()
    myEng.updateBoard(board)
    print(board)



    transport, engine = await chess.engine.popen_uci("stockfish\stockfish_14_x64_avx2.exe")
    while(not board.is_game_over()):
        curMove = myEng.makeMove()
        print(curMove)
        # board.push(curMove)
        board.push(curMove)
        print(board)
        if(board.is_game_over()):
            break
        engMove = await engine.play(board, chess.engine.Limit(time=.1))
        print(engMove.move)
        board.push(engMove.move)

    await engine.quit()
    print(board.outcome())
    myEng.passResult(board.outcome())


asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())