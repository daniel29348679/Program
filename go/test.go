package main

import (
	"log"
	"sync"
)

// 不能讓發布者或是訂閱者來關閉資料通道, 且不能讓發布者這邊來關閉額外的訊息通道來通知其他所有角色退出.
// 引入主持人這角色在這情境下, 來關閉訊息通道
func main() {

	wgSubscribers := sync.WaitGroup{}
	wgSubscribers.Add(2)

	dataCh := make(chan int, 200)

	go func() {
		defer wgSubscribers.Done()
		for {
			select {
			case value := <-dataCh:
				log.Println("form core1 ", value)
				return
			default:
			}
		}
	}()

	go func() {
		defer wgSubscribers.Done()
		for {
			select {
			case value := <-dataCh:
				log.Println("form core2 ", value)
				return
			default:
			}
		}
	}()

	dataCh <- 100
	dataCh <- 200
	wgSubscribers.Wait()
	log.Println(len(dataCh))
}
