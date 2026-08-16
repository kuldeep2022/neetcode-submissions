class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        startColor = image[sr][sc]
        def dfs(r,c):
            ROW,COL = len(image), len(image[0])
            if r<0 or c<0 or r == ROW or c == COL or image[r][c] != startColor:
                return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        dfs(sr,sc) 
        #print("Image after change", image)

        return image
        